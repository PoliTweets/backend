# coding=utf-8
from django.conf import settings

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import models
import forms
import random

NUMBER_OF_TWEETS_PER_PARTY = 2
NUMBER_OF_PARTY = 7 # Must match the reality of DB...

def index(request):
    context = RequestContext(request)
    context_dict = {"title": u"Politweets Bienvenue"}
    return render_to_response('politweets/index.html', context_dict, context)


def round(request):
    context = RequestContext(request)
    TOTAL_NUMBER_OF_TWEETS = NUMBER_OF_TWEETS_PER_PARTY*NUMBER_OF_PARTY

    # Huh? http://stackoverflow.com/questions/16370339/django-1-5-session-key-is-none
    if not request.session.get('has_session'):
        request.session['has_session'] = True

    if request.method == 'GET':
        sessionid = request.session.session_key
        print " > Session ID:", sessionid

        # At this stage, we may or may not have a session ID

        index = 1
        round = None

        if sessionid is not None: # Handle case WITH sesssion ID
            round, created = models.Round.objects.get_or_create(sessionid=sessionid)
            index = round.results.count() + 1

            if index > TOTAL_NUMBER_OF_TWEETS:
                request.session.flush()

                total_count, party_counts = round.correct_answers()
                context_dict = {"title": u"Politweets Résultats",
                                "total_count": total_count,
                                "party_counts": party_counts,
                                "tweet_count_per_party": NUMBER_OF_TWEETS_PER_PARTY,
                                "total_tweets_count": TOTAL_NUMBER_OF_TWEETS}

                return render_to_response('politweets/results.html', context_dict, context)

        tweet = get_next_tweet_for_round(round)
        candidate, choices = get_candidate_choices_for_tweet(tweet)

        form = forms.ResultCreateForm(choices=choices)
        context_dict = {"title": "Politweets",
                        "form": form,
                        "tweet": tweet,
                        "candidate": candidate,
                        "index": index,
                        "total": TOTAL_NUMBER_OF_TWEETS}

        return render_to_response('politweets/round.html', context_dict, context)

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

        return HttpResponseRedirect(reverse_lazy('politweets:round'))



def get_next_tweet_for_round(round=None):
    if round is None or round.results.count() == 0:
        return models.Tweet.objects.order_by("?").first()

    round_tweets_ids = [ r.tweet.tweet_id for r in round.results.all() ]
    valid_tweets = models.Tweet.objects.exclude(tweet_id__in=round_tweets_ids).order_by("?")
    valid_parties = list(round.parties_with_incomplete_results(NUMBER_OF_TWEETS_PER_PARTY))

    for tweet in valid_tweets.all():
        candidate = models.Candidate.objects.get(handle=tweet.handle)
        party = models.Party.objects.get(key=candidate.party_key)

        if candidate.party is None: # Candidates are not loaded with their associated party, but only their party key.
            candidate.party = party
            candidate.save()

        if party in valid_parties:
            return tweet


def get_candidate_choices_for_tweet(tweet):
    candidate = models.Candidate.objects.get(handle=tweet.handle)
    assert candidate is not None, "Candidate is None?"

    expected_party = models.Party.objects.get(key=candidate.party_key)
    assert expected_party is not None, "Party is None?"

    CHOICES = [
        (expected_party.key, models.PARTY_CHOICES_DICT[expected_party.key]),
    ]

    for i in range(20):
        new_choice = random.choice(models.PARTY_CHOICES)
        if new_choice not in CHOICES and new_choice[0] != "unk":
            CHOICES.append(new_choice)
        if len(CHOICES) == 4:
            break

    random.shuffle(CHOICES)
    return candidate, CHOICES

