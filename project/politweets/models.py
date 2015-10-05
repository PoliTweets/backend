# coding=utf-8

from django.conf import settings
from django.db import models

PARTY_UNDEFINED = "unk"
PARTY_UDC = "udc"
PARTY_PLR = "plr"
PARTY_PDC = "pdc"
PARTY_PS = "ps"
PARTY_GREEN = "gre"
PARTY_GREEN_LIB = "lib"
PARTY_PBD = "pbd"

PARTY_CHOICES_KEYS = (
    PARTY_UNDEFINED,
    PARTY_UDC,
    PARTY_PLR,
    PARTY_PDC,
    PARTY_PS,
    PARTY_GREEN,
    PARTY_GREEN_LIB,
    PARTY_PBD
)

PARTY_CHOICES_VALUE = (
    u"Indéfini",
    "UDC",
    "PLR",
    "PDC",
    "PS",
    "Les Verts",
    u"Vert'libéraux",
    "PBD"
)

PARTY_CHOICES = tuple(zip(PARTY_CHOICES_KEYS, PARTY_CHOICES_VALUE))
PARTY_CHOICES_DICT = dict(zip(PARTY_CHOICES_KEYS, PARTY_CHOICES_VALUE))

class Tweet(models.Model):
    handle = models.CharField(max_length=100, null=True, blank=True)
    tweet_id = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=240, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return u"Tweet ("+self.tweet_id+", "+self.handle+")"


class Party(models.Model):
    key = models.CharField(max_length=3, choices=PARTY_CHOICES, default=PARTY_UNDEFINED)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    logo_url = models.URLField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return u"Party ("+self.key+")"


class Candidate(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    handle = models.CharField(max_length=100, null=True, blank=True)
    canton = models.CharField(max_length=10, null=True, blank=True)
    party = models.ForeignKey(Party, blank=True, null=True, default=None, related_name='candidates')
    party_key = models.CharField(max_length=3, null=True, blank=True)
    full_party_name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u"Candidate: "+self.handle+" ("+self.name+")"


class Round(models.Model):
    sessionid = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    affinity_party = models.CharField(max_length=3, choices=PARTY_CHOICES, default=PARTY_UNDEFINED)

    def __unicode__(self):
        return u"Round ("+self.sessionid+")"

    def correct_answers(self):
        party_counts = {}

        for party in Party.objects.all():
            party_counts[PARTY_CHOICES_DICT[party.key]] = 0

        total_count = 0
        for result in self.results.all():
            if result.is_answer_correct():
                total_count += 1
                party_counts[PARTY_CHOICES_DICT[result.answered_party.key]] += 1

        # Changing to string to avoid some issues.
        for key in party_counts.keys():
            party_counts[key] = str(party_counts[key])

        return total_count, party_counts

    def parties_with_incomplete_results(self, number_of_results_per_party):
        tmp = []

        if number_of_results_per_party > 0:
            for party in Party.objects.all():
                existing_results = Result.objects.filter(round=self, answered_party=party)
                if existing_results.count() < number_of_results_per_party:
                    tmp.append(party)

        return tmp


class Result(models.Model):
    round = models.ForeignKey(Round, blank=True, null=True, default=None, related_name='results')
    tweet = models.ForeignKey(Tweet, blank=True, null=True, default=None, related_name='results')
    answered_party = models.ForeignKey(Party, blank=True, null=True, default=None, related_name='answers')

    def is_answer_correct(self):
        candidate = Candidate.objects.get(handle=self.tweet.handle)

        if candidate.party is None and candidate.party_key is not None:
            party = Party.objects.get(key=candidate.party_key)
            candidate.party = party
            candidate.save()

        return self.answered_party == candidate.party

    def __unicode__(self):
        return u"Result ("+self.round+", "+self.tweet+", "+self.answered_party+")"
