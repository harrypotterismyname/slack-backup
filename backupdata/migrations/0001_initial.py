# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('topic', models.TextField(default=b'')),
                ('purpose', models.TextField(default=b'')),
                ('slack_id', models.CharField(default=b'', max_length=10)),
                ('creator_slack_id', models.CharField(default=b'', max_length=10)),
                ('next_crawl_time', models.DateTimeField(auto_now_add=True)),
                ('next_crawl_cycle', models.IntegerField(default=1)),
                ('is_privategroup', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('latest_crawled', models.DateTimeField(null=True)),
                ('oldest_crawled', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_type', models.CharField(default=b'', max_length=50, db_index=True)),
                ('message_subtype', models.CharField(default=b'', max_length=50, db_index=True)),
                ('hidden', models.BooleanField(default=False)),
                ('ts', models.DateTimeField(null=True, db_index=True)),
                ('deleted_ts', models.DateTimeField(null=True)),
                ('event_ts', models.DateTimeField(null=True)),
                ('user_slack_id', models.CharField(default=b'', max_length=10, db_index=True)),
                ('text', models.TextField(default=b'')),
                ('channel', models.ForeignKey(to='backupdata.Channel', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
