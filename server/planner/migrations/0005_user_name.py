# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20170224_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='name'),
        ),
    ]
