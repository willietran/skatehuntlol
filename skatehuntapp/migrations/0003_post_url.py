# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skatehuntapp', '0002_auto_20150322_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(default=0, max_length=140),
            preserve_default=False,
        ),
    ]
