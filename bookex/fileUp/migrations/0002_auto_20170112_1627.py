# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileUp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='descrption'),
        ),
    ]
