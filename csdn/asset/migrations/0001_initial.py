# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=80, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xbc\x96\xe7\xa0\x81')),
                ('name', models.CharField(max_length=80, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('brand', models.CharField(max_length=80, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('type', models.CharField(max_length=80, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('department', models.CharField(max_length=80, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('user', models.CharField(max_length=80, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xba\xba')),
                ('statue', models.CharField(max_length=80, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('location', models.CharField(max_length=80, verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe4\xbd\x8d\xe7\xbd\xae')),
                ('delivery_time', models.CharField(max_length=80, verbose_name=b'\xe5\x87\xba\xe5\x8e\x82\xe6\x97\xb6\xe9\x97\xb4')),
                ('remark', models.CharField(max_length=80, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
        ),
    ]
