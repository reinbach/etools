# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-07 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publics', '0002_auto_20170206_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessarea',
            name='default_currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Currency'),
        ),
    ]
