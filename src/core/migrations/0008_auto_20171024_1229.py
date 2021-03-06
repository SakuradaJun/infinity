# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-24 12:29
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171024_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), blank=True, default=[], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), blank=True, default=[], size=None),
            preserve_default=False,
        ),
    ]
