# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20170224_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.TextField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='planner.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.User')),
            ],
        ),
        migrations.CreateModel(
            name='PresentIdeaComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='planner.User')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.PresentIdea')),
            ],
        ),
        migrations.CreateModel(
            name='PresentIdeaUpvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='planner.User')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.PresentIdea')),
            ],
        ),
    ]