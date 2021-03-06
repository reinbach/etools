# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-13 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0019_auto_20170208_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovernmentInterventionResultActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=36)),
                ('description', models.CharField(max_length=1024)),
                ('intervention_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_activities', to='partners.GovernmentInterventionResult')),
            ],
        ),
    ]
