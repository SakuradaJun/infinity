# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170818_1724'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thing',
            new_name='Item',
        ),
    ]