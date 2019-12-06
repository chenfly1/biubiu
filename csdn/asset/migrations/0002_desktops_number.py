# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktops',
            name='number',
            field=models.CharField(default=1, max_length=80, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f'),
            preserve_default=False,
        ),
    ]
