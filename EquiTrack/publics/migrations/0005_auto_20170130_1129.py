# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-30 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publics', '0004_auto_20170127_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='threshold_tae_usd',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='threshold_tre_usd',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
