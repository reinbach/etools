# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-23 09:11
from __future__ import unicode_literals
import datetime

from django.db import migrations


def set_clearances_for_old_trips(apps, schema_editor):
    """ Migration of old trips failed to create related
        Clearances (which default to not_applicable),
        so old trips can't be completed.

        https://github.com/unicef/etools-issues/issues/166
    """

    Travel = apps.get_model("t2f", "Travel")
    Clearances = apps.get_model("t2f", "Clearances")

    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    for travel in Travel.objects.filter(created__gt=six_months_ago):
        if not hasattr(travel, 'clearances'):
            # creating Clearances
            clearances = Clearances(travel=travel)
            clearances.save()
        else:
            pass


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('t2f', '0009_auto_20170324_1121'),
    ]

    operations = [
            migrations.RunPython(set_clearances_for_old_trips, reverse),
    ]
