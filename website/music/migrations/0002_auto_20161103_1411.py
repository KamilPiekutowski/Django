# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='gebre',
            new_name='genre',
        ),
    ]
