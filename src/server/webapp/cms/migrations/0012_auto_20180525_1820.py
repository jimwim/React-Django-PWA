# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20180525_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('google_link', models.URLField(blank=True, max_length=255, null=True)),
                ('github_link', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram_link', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedin_link', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Footers',
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='contactme',
            name='image',
        ),
    ]
