# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-17 20:17
from __future__ import unicode_literals

from django.db import migrations, models, connection
from django.db.models import Sum
def reverse(apps, schema_editor):
    pass

def migrate_planned_budget(apps, schema_editor):
    InterventionBudget = apps.get_model('partners', 'InterventionBudget')
    Intervention = apps.get_model('partners', 'Intervention')
    Workspace = apps.get_model('users', 'Country')
    current_workspace = Workspace.objects.get(schema_name=connection.schema_name)

    if not current_workspace.schema_name == 'test':
        assert current_workspace.local_currency is not None

    local_currency = current_workspace.local_currency
    interventions = Intervention.objects.all()
    print("Total interventions {}".format(interventions.count()))
    count = 0
    for i in interventions:
        if i.planned_budget.exists():
            pb = i.planned_budget.aggregate(
                total_partner_contribution=Sum('partner_contribution'),
                total_unicef_cash=Sum('unicef_cash'),
                total_in_kind_amount=Sum('in_kind_amount'),
                total_partner_contribution_local=Sum('partner_contribution_local'),
                total_unicef_cash_local=Sum('unicef_cash_local'),
                total_in_kind_amount_local=Sum('in_kind_amount_local')
            )
            currency = i.planned_budget.first().currency or local_currency
            i.planned_budget.all().delete()

            new_planned_budget = InterventionBudget(
                intervention=i,
                partner_contribution=pb['total_partner_contribution'],
                unicef_cash=pb['total_unicef_cash'],
                in_kind_amount=pb['total_in_kind_amount'],
                partner_contribution_local=pb['total_partner_contribution_local'],
                unicef_cash_local=pb['total_unicef_cash_local'],
                in_kind_amount_local=pb['total_in_kind_amount_local'],
                total=pb['total_partner_contribution'] + pb['total_in_kind_amount'] + pb['total_unicef_cash'],
                currency=currency,
            )
            new_planned_budget.save()
            count += 1
        else:
            new_planned_budget = InterventionBudget(
                intervention=i,
                partner_contribution=0,
                unicef_cash=0,
                in_kind_amount=0,
                partner_contribution_local=0,
                unicef_cash_local=0,
                in_kind_amount_local=0,
                currency=local_currency,
                total=0
            )
            new_planned_budget.save()

        print('Updated automatically {}'.format(count))


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0030_intervention_signed_pd_document'),
        ('users', '0008_workspacecounter'),
        ('publics', '0024_auto_20170526_1600')
    ]
    operations = [
        migrations.RunPython(
            migrate_planned_budget, reverse_code=reverse),
    ]

