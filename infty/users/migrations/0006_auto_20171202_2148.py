# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-02 21:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171112_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onetimepassword',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='onetimepassword',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 12, 2, 21, 48, 3, 927387)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]