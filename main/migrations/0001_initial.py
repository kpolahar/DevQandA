# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-04 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('developer_name', models.CharField(max_length=64, verbose_name=b'Name')),
                ('developer_title', models.TextField(max_length=128, verbose_name=b'Title')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('question_Q', models.TextField(max_length=256, verbose_name=b'Question')),
                ('question_A', models.TextField(max_length=512, verbose_name=b'Answer')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Developer')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
