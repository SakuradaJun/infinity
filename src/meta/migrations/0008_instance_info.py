# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 13:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0007_auto_20180201_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
