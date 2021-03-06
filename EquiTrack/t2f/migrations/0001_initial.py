# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-02 21:53
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import t2f.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publics', '0001_initial'),
        ('partners', '0017_remove_bankdetails_agreement'),
        ('locations', '0004_auto_20170112_2051'),
        ('users', '0004_auto_20170201_1731'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0003_auto_20161227_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_point_number', models.CharField(default=t2f.models.make_action_point_number, max_length=11, unique=True)),
                ('description', models.CharField(max_length=254)),
                ('due_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=254, null=True, verbose_name='Status')),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('actions_taken', models.TextField(blank=True, null=True)),
                ('follow_up', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('person_responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clearances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_clearance', models.CharField(choices=[('requested', 'requested'), ('not_requested', 'not_requested'), ('not_applicable', 'not_applicable')], default='not_applicable', max_length=14)),
                ('security_clearance', models.CharField(choices=[('requested', 'requested'), ('not_requested', 'not_requested'), ('not_applicable', 'not_applicable')], default='not_applicable', max_length=14)),
                ('security_course', models.CharField(choices=[('requested', 'requested'), ('not_requested', 'not_requested'), ('not_applicable', 'not_applicable')], default='not_applicable', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='CostAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.PositiveIntegerField()),
                ('delegate', models.BooleanField(default=False)),
                ('business_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.BusinessArea')),
                ('fund', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Fund')),
                ('grant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Grant')),
            ],
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('breakfast', models.BooleanField(default=False)),
                ('lunch', models.BooleanField(default=False)),
                ('dinner', models.BooleanField(default=False)),
                ('accomodation', models.BooleanField(default=False)),
                ('no_dsa', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('account_currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Currency')),
                ('document_currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=32, unique=True)),
                ('business_area', models.CharField(max_length=32)),
                ('vendor_number', models.CharField(max_length=32)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('success', 'Success'), ('error', 'Error')], max_length=16)),
                ('message', models.TextField(blank=True, null=True)),
                ('vision_fi_id', models.CharField(blank=True, max_length=16, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fund', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Fund')),
                ('grant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Grant')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='t2f.Invoice')),
                ('wbs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.WBS')),
            ],
        ),
        migrations.CreateModel(
            name='IteneraryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('overnight_travel', models.BooleanField(default=False)),
                ('mode_of_travel', models.CharField(choices=[('Plane', 'Plane'), ('Bus', 'Bus'), ('Car', 'Car'), ('Boat', 'Boat'), ('Rail', 'Rail')], max_length=5, null=True)),
                ('airlines', models.ManyToManyField(related_name='_iteneraryitem_airlines_+', to='publics.AirlineCompany')),
                ('dsa_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.DSARegion')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('canceled_at', models.DateTimeField(null=True)),
                ('submitted_at', models.DateTimeField(null=True)),
                ('rejected_at', models.DateTimeField(null=True)),
                ('approved_at', models.DateTimeField(null=True)),
                ('rejection_note', models.TextField(null=True)),
                ('cancellation_note', models.TextField(null=True)),
                ('certification_note', models.TextField(null=True)),
                ('report_note', models.TextField(null=True)),
                ('misc_expenses', models.TextField(null=True)),
                ('status', django_fsm.FSMField(choices=[('planned', 'Planned'), ('submitted', 'Submitted'), ('rejected', 'Rejected'), ('approved', 'Approved'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('sent_for_payment', 'Sent for payment'), ('certification_submitted', 'Certification submitted'), ('certification_approved', 'Certification approved'), ('certification_rejected', 'Certification rejected'), ('certified', 'Certified'), ('completed', 'Completed')], default='planned', max_length=50, protected=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('purpose', models.CharField(blank=True, max_length=500, null=True)),
                ('additional_note', models.TextField(blank=True, null=True)),
                ('international_travel', models.NullBooleanField(default=False)),
                ('ta_required', models.NullBooleanField(default=True)),
                ('reference_number', models.CharField(default=t2f.models.make_travel_reference_number, max_length=12, unique=True)),
                ('hidden', models.BooleanField(default=False)),
                ('mode_of_travel', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Plane', 'Plane'), ('Bus', 'Bus'), ('Car', 'Car'), ('Boat', 'Boat'), ('Rail', 'Rail')], max_length=5), null=True, size=None)),
                ('estimated_travel_cost', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('is_driver', models.BooleanField(default=False)),
                ('preserved_expenses', models.DecimalField(decimal_places=4, default=None, max_digits=20, null=True)),
                ('approved_cost_traveler', models.DecimalField(decimal_places=4, default=None, max_digits=20, null=True)),
                ('approved_cost_travel_agencies', models.DecimalField(decimal_places=4, default=None, max_digits=20, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.Currency')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.Office')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.Section')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('traveler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='travels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TravelActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_type', models.CharField(choices=[('Programmatic Visit', 'Programmatic Visit'), ('Spot Check', 'Spot Check'), ('Advocacy', 'Advocacy'), ('Technical Support', 'Technical Support'), ('Meeting', 'Meeting'), ('Staff Development', 'Staff Development'), ('Staff Entitlement', 'Staff Entitlement')], max_length=64, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('locations', models.ManyToManyField(related_name='_travelactivity_locations_+', to='locations.Location')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='partners.PartnerOrganization')),
                ('partnership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='partners.Intervention')),
                ('primary_traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reports.Result')),
                ('travels', models.ManyToManyField(related_name='activities', to='t2f.Travel')),
            ],
        ),
        migrations.CreateModel(
            name='TravelAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=t2f.models.determine_file_upload_path)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='t2f.Travel')),
            ],
        ),
        migrations.CreateModel(
            name='TravelPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=50)),
                ('usage_place', models.CharField(choices=[('travel', 'Travel'), ('action_point', 'Action point')], max_length=12)),
                ('user_type', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=128)),
                ('field', models.CharField(max_length=64)),
                ('permission_type', models.CharField(choices=[('edit', 'Edit'), ('view', 'View')], max_length=5)),
                ('value', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='iteneraryitem',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary', to='t2f.Travel'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='t2f.Travel'),
        ),
        migrations.AddField(
            model_name='expense',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='t2f.Travel'),
        ),
        migrations.AddField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.TravelExpenseType'),
        ),
        migrations.AddField(
            model_name='deduction',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deductions', to='t2f.Travel'),
        ),
        migrations.AddField(
            model_name='costassignment',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_assignments', to='t2f.Travel'),
        ),
        migrations.AddField(
            model_name='costassignment',
            name='wbs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publics.WBS'),
        ),
        migrations.AddField(
            model_name='clearances',
            name='travel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clearances', to='t2f.Travel'),
        ),
        migrations.AddField(
            model_name='actionpoint',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_points', to='t2f.Travel'),
        ),
    ]
