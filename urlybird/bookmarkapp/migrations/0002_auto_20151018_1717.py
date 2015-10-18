# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='short_url',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
