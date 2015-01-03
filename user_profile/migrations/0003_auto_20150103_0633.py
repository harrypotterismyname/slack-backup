# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20150103_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slack_username',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
