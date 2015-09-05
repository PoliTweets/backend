# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0005_auto_20150904_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='sessionid',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
