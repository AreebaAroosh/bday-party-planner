# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_auto_20170224_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]