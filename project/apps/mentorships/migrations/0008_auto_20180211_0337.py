# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorships', '0007_auto_20180211_0220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrole',
            options={'ordering': ('university_session', 'is_active', 'user__user__gender', 'user__gender_mode')},
        ),
        migrations.AlterField(
            model_name='useruniversity',
            name='gender_mode',
            field=models.CharField(blank=True, choices=[('0', 'Definitely'), ('1', 'If possible'), ('9', 'Unconcerned')], max_length=16, verbose_name='Gender Mode'),
        ),
    ]
