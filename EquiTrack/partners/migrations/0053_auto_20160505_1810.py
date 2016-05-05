# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0052_convert_disaggregation_to_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultchain',
            name='disaggregation',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
