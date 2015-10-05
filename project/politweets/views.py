from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import models
import forms
import random

def index(request):
    context = RequestContext(request)

    if request.method == 'GET':
        sessionid = request.session.session_key

        round, created = models.Round.objects.get_or_create(sessionid=sessionid)
        index = round.results.count() + 1
        if index == 11:
            request.session.flush()
            return HttpResponseRedirect(reverse('index'))

        # Automatic filtering out of empty result.
        for r in round.results.all():
            if r.answered_party is None:
                r.delete()

        if round.results.count() == 0:
            tweet = models.Tweet.objects.order_by("?").first()
        else:
            round_tweets_ids = [ r.tweet.tweet_id for r in round.results.all() ]
            tweet = models.Tweet.objects.exclude(tweet_id__in=round_tweets_ids).order_by("?").first()

        candidates = models.Candidate.objects.filter(handle=tweet.handle)
        candidate = candidates.first()

        # Automatic cleaning of duplicates in case DB wasn't loaded correctly
        if candidates.count() > 1:
            for candidate in candidates.all()[1:]:
                candidate.delete()

        if candidate.party_name is None:
            party_name_key = None
            for key in models.PARTY_CHOICES_KEYS:
                if candidate.full_party_name is not None and key in candidate.full_party_name:
                    party_name_key = key
                    break
        else:
            INVERTED_PARTY_CHOICES = dict(zip(models.PARTY_CHOICES_VALUE, models.PARTY_CHOICES_KEYS))
            party_name_key = INVERTED_PARTY_CHOICES[candidate.party_name]

        if settings.DEBUG and party_name_key is None:
            party_name_key = "ps"

        expected_party = models.Party.objects.get(name=party_name_key)

        PARTY_CHOICES_DICT = dict(zip(models.PARTY_CHOICES_KEYS, models.PARTY_CHOICES_VALUE))
        CHOICES = (
            (expected_party.name, PARTY_CHOICES_DICT[expected_party.name]),
        )

        for i in range(20):
            new_choice = random.choice(models.PARTY_CHOICES)
            if new_choice not in CHOICES and new_choice[0] != "unk":
                CHOICES += (new_choice,)
            if len(CHOICES) == 4:
                break


        form = forms.ResultCreateForm(answer=CHOICES)
        context_dict = {"title": "Politweets", "form": form, "tweet": tweet, "candidate": candidate, "index": index, "party_name_key": party_name_key}
        return render_to_response('politweets/index.html', context_dict, context)
    else:


        form = forms.ResultCreateForm() # Bind data from request.POST into a PostForm
        #
        # if form.is_valid():
        #     answer = form.cleaned_data['answer']
        #     return HttpResponseRedirect(reverse('index'))

        context_dict = {"title": "Politweets", "form": form}
        return render_to_response(request, 'politweets/index.html', context_dict, context)

