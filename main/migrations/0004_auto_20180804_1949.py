# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-05 00:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180804_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='first_name',
            field=models.CharField(blank=True, max_length=32, verbose_name=b'First Name'),
        ),
        migrations.AddField(
            model_name='developer',
            name='last_name',
            field=models.CharField(blank=True, max_length=32, verbose_name=b'Last Name'),
        ),
        migrations.AddField(
            model_name='qanda',
            name='qanda_id',
            field=models.CharField(default=datetime.datetime.now, help_text=b'Please give this a unique QandA ID, using 16 characters or fewer.', max_length=16, unique=True, verbose_name=b'QandA ID'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(blank=True, max_length=65, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='title',
            field=models.TextField(blank=True, max_length=128, verbose_name=b'Title'),
        ),
        migrations.AlterField(
            model_name='qanda',
            name='answer',
            field=models.TextField(blank=True, max_length=512, verbose_name=b'Answer'),
        ),
        migrations.AlterField(
            model_name='qanda',
            name='developer_id',
            field=models.CharField(blank=True, help_text=b'Please give your unique 16 character developer ID to ensure this QandA is saved to your developer profile.', max_length=16, verbose_name=b'Developer ID'),
        ),
        migrations.AlterField(
            model_name='qanda',
            name='question',
            field=models.TextField(blank=True, max_length=256, verbose_name=b'Question'),
        ),
    ]
