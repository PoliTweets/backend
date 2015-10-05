# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politweets', '0011_auto_20151005_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='category',
        ),
        migrations.RemoveField(
            model_name='round',
            name='affinity_category',
        ),
        migrations.AddField(
            model_name='round',
            name='affinity_party',
            field=models.CharField(default=b'unk', max_length=3, choices=[(b'unk', 'Ind\xe9fini'), (b'udc', b'UDC'), (b'plr', b'PLR'), (b'pdc', b'PDC'), (b'ps', b'PS'), (b'gre', b'Les Verts'), (b'lib', "Vert'lib\xe9raux"), (b'pbd', b'PBD')]),
        ),
    ]
