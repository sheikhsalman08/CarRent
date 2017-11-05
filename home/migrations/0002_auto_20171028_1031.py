# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'', blank=True)),
                ('model', models.CharField(blank=True, max_length=40, null=True, choices=[('1', 'Perodua Myvi'), ('2', 'Perodua Alza'), ('3', 'Perodua Axia'), ('4', 'Honda City'), ('5', 'Honda Civic')])),
                ('seat', models.IntegerField(default=5)),
                ('ac', models.BooleanField(default=True)),
                ('availability', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=240, null=True, blank=True)),
                ('per_hour', models.IntegerField(default=10)),
                ('SpacialDiscount', models.CharField(max_length=240, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='car_owner', to='home.CarOwner')),
            ],
        ),
        migrations.RemoveField(
            model_name='cars',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
    ]
