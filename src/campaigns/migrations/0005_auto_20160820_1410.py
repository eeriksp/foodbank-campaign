# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_auto_20160820_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignlocationshift',
            name='volunteers',
            field=models.ManyToManyField(blank=True, null=True, to='volunteers.Volunteer'),
        ),
    ]