# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_topic_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='children', to='core.Topic'),
        ),
    ]
