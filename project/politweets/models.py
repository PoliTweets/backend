# coding=utf-8

from django.conf import settings
from django.db import models
from autoslug import AutoSlugField

CATEGORY_UNDEFINED = "unk"
CATEGORY_LEFT = "lef"
CATEGORY_CENTER = "cen"
CATEGORY_RIGHT = "rig"

CATEGORY_KEYS = (
    CATEGORY_UNDEFINED,
    CATEGORY_LEFT,
    CATEGORY_CENTER,
    CATEGORY_RIGHT
)

CATEGORY_VALUES = (
    u"Indéfini",
    "Gauche",
    "Centre",
    "Droite"
)

CATEGORY_CHOICES = tuple(zip(CATEGORY_KEYS, CATEGORY_VALUES))

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

class Tweet(models.Model):
    handle = models.CharField(max_length=100, null=True, blank=True)
    tweet_id = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=240, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)


class Party(models.Model):
    name = models.CharField(max_length=3, choices=PARTY_CHOICES, default=PARTY_UNDEFINED)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    logo_url = models.URLField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=CATEGORY_UNDEFINED)


class Candidate(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    handle = models.CharField(max_length=100, null=True, blank=True)
    canton = models.CharField(max_length=10, null=True, blank=True)
    party = models.ForeignKey(Party, blank=True, null=True, default=None, related_name='candidates')
    full_party_name = models.CharField(max_length=100, null=True, blank=True)
    party_name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "Candidate: "+self.handle+" ("+self.name+")"

class Round(models.Model):
    sessionid = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='start_date', unique_with='start_date')
    affinity_category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=CATEGORY_UNDEFINED)


class Result(models.Model):
    round = models.ForeignKey(Round, blank=True, null=True, default=None, related_name='results')
    tweet = models.ForeignKey(Tweet, blank=True, null=True, default=None, related_name='results')
    answered_party = models.ForeignKey(Party, blank=True, null=True, default=None, related_name='answers')


