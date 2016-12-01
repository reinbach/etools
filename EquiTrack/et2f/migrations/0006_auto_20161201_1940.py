# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-01 17:40
from __future__ import unicode_literals

from django.db import migrations

from et2f.models import TravelType as TravelTypeModel, ModeOfTravel as ModeOfTravelModel


def reset_travel_type_relations(apps, schema_editor):
    Travel = apps.get_model('et2f', 'Travel')
    IteneraryItem = apps.get_model('et2f', 'IteneraryItem')
    TravelActivity = apps.get_model('et2f', 'TravelActivity')
    ModeOfTravel = apps.get_model('et2f', 'ModeOfTravel')
    TravelType = apps.get_model('et2f', 'TravelType')

    mode_of_travel = ModeOfTravel.objects.last()
    travel_type = TravelType.objects.last()
    for t in Travel.objects.all():
        t.mode_of_travel.clear()
    IteneraryItem.objects.all().update(mode_of_travel=mode_of_travel)
    TravelActivity.objects.all().update(travel_type=None)


def create_travel_type_models(apps, schema_editor):
    TravelType = apps.get_model('et2f', 'TravelType')

    TravelType.objects.all().delete()
    for choice in TravelTypeModel.CHOICES:
        TravelType.objects.create(name=choice[0])


def create_mode_of_travel_models(apps, schema_editor):
    ModeOfTravel = apps.get_model('et2f', 'ModeOfTravel')

    for choice in ModeOfTravelModel.CHOICES:
        ModeOfTravel.objects.create(name=choice[0])


class Migration(migrations.Migration):

    dependencies = [
        ('et2f', '0005_auto_20161201_1926'),
    ]

    operations = [
        migrations.RunPython(create_mode_of_travel_models),
        migrations.RunPython(create_travel_type_models),
        migrations.RunPython(reset_travel_type_relations),
    ]
