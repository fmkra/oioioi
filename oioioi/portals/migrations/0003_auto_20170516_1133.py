# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-16 11:33
from __future__ import unicode_literals

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0002_node_problems_in_content'),
    ]

    operations = [
        # Previously this migration was a migrations.AlterModelManagers,
        # but the _base_manager attribute was removed and this errors
        # on Django1.10
    ]
