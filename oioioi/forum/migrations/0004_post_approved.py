# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-21 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_ban'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='approved'),
        ),
    ]
