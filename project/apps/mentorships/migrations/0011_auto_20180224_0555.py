# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentorships', '0010_auto_20180224_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentee', to='mentorships.UserRole'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='mentorships.UserRole'),
        ),
    ]
