# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_party_created_dt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PresentIdea',
            new_name='GiftIdea',
        ),
        migrations.RenameModel(
            old_name='PresentIdeaComment',
            new_name='GiftIdeaComment',
        ),
        migrations.RenameModel(
            old_name='PresentIdeaUpvote',
            new_name='GiftIdeaUpvote',
        ),
    ]
