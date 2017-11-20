# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 02:51
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171030_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='address_text',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='carowner',
            name='address_text',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True),
        ),
    ]