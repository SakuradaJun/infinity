# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-16 15:58
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170903_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('code_name', models.CharField(max_length=10)),
                ('code_number', models.IntegerField()),
                ('endpoint', models.TextField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('data_format_name', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
