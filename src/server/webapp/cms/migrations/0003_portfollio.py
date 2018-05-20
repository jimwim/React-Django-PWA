# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('cms', '0002_auto_20180417_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfollio',
            fields=[
                ('basemodule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.BaseModule')),
                ('text', models.CharField(max_length=255)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
            bases=('cms.basemodule',),
        ),
    ]
