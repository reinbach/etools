# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-21 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('et2f', '0031_auto_20161121_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteneraryitem',
            name='mode_of_travel',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='mode_of_travel',
        ),
        migrations.RemoveField(
            model_name='travelactivity',
            name='travel_type',
        ),

        migrations.RenameField(
            model_name='iteneraryitem',
            old_name='new_mode_of_travel',
            new_name='mode_of_travel',
        ),
        migrations.RenameField(
            model_name='travelactivity',
            old_name='new_travel_type',
            new_name='travel_type',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='new_mode_of_travel',
            new_name='mode_of_travel',
        ),
    ]
