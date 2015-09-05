# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0008_candidate_full_party_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='party_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
