# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0002_auto_20150904_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tweet_time',
            new_name='date',
        ),
    ]
