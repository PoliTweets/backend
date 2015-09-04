# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('handle', models.CharField(max_length=100, null=True, blank=True)),
                ('canton', models.CharField(max_length=2, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(default=b'unk', max_length=3, choices=[(b'unk', 'Ind\xe9fini'), (b'udc', b'UDC'), (b'plr', b'PLR'), (b'pdc', b'PDC'), (b'ps', b'PS'), (b'gre', b'Les Verts'), (b'lib', 'Verts Lib\xe9raux'), (b'pbd', b'PBD')])),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('logo_url', models.URLField(null=True, blank=True)),
                ('category', models.CharField(default=b'unk', max_length=3, choices=[(b'unk', 'Ind\xe9fini'), (b'lef', b'Gauche'), (b'cen', b'Centre'), (b'rig', b'Droite')])),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answered_party', models.ForeignKey(related_name='answers', default=None, blank=True, to='politweets.Party', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('affinity_category', models.CharField(default=b'unk', max_length=3, choices=[(b'unk', 'Ind\xe9fini'), (b'lef', b'Gauche'), (b'cen', b'Centre'), (b'rig', b'Droite')])),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle', models.CharField(max_length=100, null=True, blank=True)),
                ('tweet_id', models.CharField(max_length=100, null=True, blank=True)),
                ('text', models.CharField(max_length=240, null=True, blank=True)),
                ('tweet_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='round',
            field=models.ForeignKey(related_name='results', default=None, blank=True, to='politweets.Round', null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='tweet',
            field=models.ForeignKey(related_name='results', default=None, blank=True, to='politweets.Tweet', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(related_name='candidates', default=None, blank=True, to='politweets.Party', null=True),
        ),
    ]
