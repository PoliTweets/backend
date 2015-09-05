# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0006_round_sessionid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='short_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='full_party_name',
        ),
    ]
