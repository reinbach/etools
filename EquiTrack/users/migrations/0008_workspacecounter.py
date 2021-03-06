# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-10 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def create_counters(apps, schema_editor):
    Workspace = apps.get_model('users', 'Country')
    WorkspaceCounter = apps.get_model('users', 'WorkspaceCounter')

    for workspace in Workspace.objects.all():
        WorkspaceCounter.objects.create(workspace=workspace)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_country_long_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkspaceCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_reference_number_counter', models.PositiveIntegerField(default=1)),
                ('travel_invoice_reference_number_counter', models.PositiveIntegerField(default=1)),
                ('workspace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='users.Country')),
            ],
        ),
        migrations.RunPython(create_counters),
    ]
