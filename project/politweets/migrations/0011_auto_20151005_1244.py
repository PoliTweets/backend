# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0010_auto_20151005_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='name',
            new_name='key',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='party_name',
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_key',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
    ]
