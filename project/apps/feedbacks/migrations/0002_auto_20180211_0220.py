# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'feedback'},
        ),
    ]
