# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(default=b'unk', max_length=3, choices=[(b'unk', 'Ind\xe9fini'), (b'udc', b'UDC'), (b'plr', b'PLR'), (b'pdc', b'PDC'), (b'ps', b'PS'), (b'gre', b'Les Verts'), (b'lib', 'Verts Lib\xe9raux'), (b'pbd', b'PBD')]),
        ),
        migrations.AlterField(
            model_name='party',
            name='short_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
