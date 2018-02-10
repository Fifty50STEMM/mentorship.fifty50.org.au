# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180209_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.CharField(blank=True, help_text='Briefly list any interests that might help in setting you up in a good mentor-mentee relationship (limit 500 chars).', max_length=512, verbose_name='Interests, hobbies or sports'),
        ),
    ]
