# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0004_candidate_full_party_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='canton',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
