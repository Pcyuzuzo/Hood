# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 09:32
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181018_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
