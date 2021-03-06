# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-17 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0028_auto_20170517_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='attached_agreement',
            field=models.FileField(blank=True, max_length=1024, upload_to=partners.models.get_agreement_path),
        ),
        migrations.AlterField(
            model_name='agreementamendment',
            name='signed_amendment',
            field=models.FileField(blank=True, max_length=1024, null=True, upload_to=partners.models.get_agreement_amd_file_path),
        ),
        migrations.AlterField(
            model_name='agreementamendmentlog',
            name='signed_document',
            field=models.FileField(blank=True, max_length=1024, null=True, upload_to=partners.models.get_agreement_amd_file_path),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='report',
            field=models.FileField(blank=True, max_length=1024, null=True, upload_to=partners.models.get_assesment_path),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='prc_review_document',
            field=models.FileField(blank=True, max_length=1024, null=True, upload_to=partners.models.get_prc_intervention_file_path),
        ),
        migrations.AlterField(
            model_name='interventionamendment',
            name='signed_amendment',
            field=models.FileField(max_length=1024, upload_to=partners.models.get_intervention_amendment_file_path),
        ),
        migrations.AlterField(
            model_name='interventionattachment',
            name='attachment',
            field=models.FileField(max_length=1024, upload_to=partners.models.get_intervention_attachments_file_path),
        ),
        migrations.AlterField(
            model_name='partnerorganization',
            name='core_values_assessment',
            field=models.FileField(blank=True, help_text='Only required for CSO partners', max_length=1024, null=True, upload_to=b'partners/core_values/'),
        ),
    ]
