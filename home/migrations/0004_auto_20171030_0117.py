# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171029_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(blank=True, choices=[('Perodua Myvi', 'Perodua Myvi'), ('Perodua Alza', 'Perodua Alza'), ('Perodua Axia', 'Perodua Axia'), ('Honda City', 'Honda City'), ('Honda Civic', 'Honda Civic')], max_length=40, null=True),
        ),
    ]