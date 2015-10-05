# coding=utf-8
from django.conf import settings

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import models
import forms
import random

NUMBER_OF_TWEETS_PER_SESSION = 2 if settings.DEBUG else 10

def index(request):
    context = RequestContext(request)

    # Huh? http://stackoverflow.com/questions/16370339/django-1-5-session-key-is-none
    if not request.session.get('has_session'):
        request.session['has_session'] = True

    if request.method == 'GET':
        sessionid = request.session.session_key
        print " > Session ID:", sessionid

        # At this stage, we may or may not have a session ID

        index = 1
        if sessionid is not None: # Handle case WITH sesssion ID
            round, created = models.Round.objects.get_or_create(sessionid=sessionid)
            index = round.results.count() + 1
            if index > NUMBER_OF_TWEETS_PER_SESSION:
                request.session.flush()
                context_dict = {"title": u"Politweets Résultats",
                                "count": len(round.correct_answers()),
                                "total": NUMBER_OF_TWEETS_PER_SESSION}
                return render_to_response('politweets/results.html', context_dict, context)

            if round.results.count() == 0:
                tweet = models.Tweet.objects.order_by("?").first()
            else:
                round_tweets_ids = [ r.tweet.tweet_id for r in round.results.all() ]
                tweet = models.Tweet.objects.exclude(tweet_id__in=round_tweets_ids).order_by("?").first()

        else:
            tweet = models.Tweet.objects.order_by("?").first()

        candidate, choices = get_candidate_choices_for_tweet(tweet)

        form = forms.ResultCreateForm(choices=choices)
        context_dict = {"title": "Politweets",
                        "form": form,
                        "tweet": tweet,
                        "candidate": candidate,
                        "index": index,
                        "total": NUMBER_OF_TWEETS_PER_SESSION}

        return render_to_response('politweets/index.html', context_dict, context)
    else:

        tweet_id = request.POST.get('tweet_id', None)
        party_key = request.POST.get('party_key', None) # answer
        sessionid = request.session.session_key
        print " < Session ID:", sessionid, tweet_id, party_key
        assert sessionid is not None, "session_id is None on POST?"

        # Get or create, as the sessionid might not have been set before.
        round, created = models.Round.objects.get_or_create(sessionid=sessionid)

        tweet = models.Tweet.objects.get(tweet_id=tweet_id)
        party = models.Party.objects.get(key=party_key)
        assert tweet is not None, "tweet is None on POST?"
        assert party is not None, "party is None on POST?"

        models.Result.objects.create(round=round, tweet=tweet, answered_party=party)

        return HttpResponseRedirect(reverse_lazy('politweets:index'))


def get_candidate_choices_for_tweet(tweet):
    candidates = models.Candidate.objects.filter(handle=tweet.handle)
    candidate = candidates.first()

    # Automatic cleaning of duplicates in case DB wasn't loaded correctly
    if candidates.count() > 1:
        for candidate in candidates.all()[1:]:
            candidate.delete()

    if candidate.party_key is None:
        for key in models.PARTY_CHOICES_KEYS:
            if candidate.full_party_name is not None and key in candidate.full_party_name.lower():
                candidate.party_key = key
                candidate.save()
                break

    expected_party = models.Party.objects.get(key=candidate.party_key)
    candidate.party = expected_party
    candidate.save()

    PARTY_CHOICES_DICT = dict(zip(models.PARTY_CHOICES_KEYS, models.PARTY_CHOICES_VALUE))
    CHOICES = [
        (expected_party.key, PARTY_CHOICES_DICT[expected_party.key]),
    ]

    for i in range(20):
        new_choice = random.choice(models.PARTY_CHOICES)
        if new_choice not in CHOICES and new_choice[0] != "unk":
            CHOICES.append(new_choice)
        if len(CHOICES) == 4:
            break

    random.shuffle(CHOICES)

    return candidate, CHOICES

