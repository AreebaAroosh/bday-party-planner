# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='deadline',
            field=models.DateField(),
        ),
    ]
