# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_add_block'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follows',
            new_name='Follow',
        ),
    ]
