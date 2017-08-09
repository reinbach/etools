# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-17 20:17
from __future__ import unicode_literals, print_function

from django.db import migrations, models, connection
from django.db.models import Sum

def reverse(apps, schema_editor):
    pass

def migrate_frs(apps, schema_editor):
    def printtf(*args):
        print('\n'.join(args))
        f = open('migration_errors.txt', 'a')
        print('\n'.join(args), file=f)
        f.close()

    FundsReservationHeader = apps.get_model('funds', 'FundsReservationHeader')
    Intervention = apps.get_model('partners', 'Intervention')
    printtf('', connection.schema_name)
    for i in Intervention.objects.all():
        fr_numbers = i.fr_numbers if i.fr_numbers else []
        for fr in fr_numbers:
            try:
                fr_obj = FundsReservationHeader.objects.get(fr_number=fr)
            except FundsReservationHeader.DoesNotExist:
                if i.status != 'draft':
                    # workaround in the local db until records are fixed in production
                    printtf('{}, {} FR not found for Intervention {}'.format(i.status, fr, i.id))
                    i.fr_numbers = None
                    i.save()
                    # raise BaseException('No FR found')
                else:
                    # if intervention is in Draft, we don't care.. we're removing FRs, let the users re-add
                    printtf('{}, {} FR not found for Intervention {}'.format(i.status, fr, i.id))
                    i.fr_numbers = None
                    i.save()
            else:
                if fr_obj.intervention and fr_obj.intervention.id != i.id:
                    printtf('#### {}, FR {} connected to a different Intervention {}... current Intervention {}'.
                            format(i.status, fr_obj.fr_number, fr_obj.intervention.id, i.id))
                    # workaround in the local db until records are fixed in production
                    i.fr_numbers = None
                    i.save()
                    # raise BaseException('FR Has been used')
                else:
                    fr_obj.intervention = i
                    fr_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0033_auto_20170614_1831'),
        ('funds', '0004_auto_20170620_0133')
    ]
    operations = [
        migrations.RunPython(
            migrate_frs, reverse_code=reverse),
    ]

