# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_auto_20180209_0236'),
        ('mentorships', '0004_auto_20180209_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='universities',
            field=models.ManyToManyField(through='mentorships.UniversitySession', to='universities.University'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='relationship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mentorships.Relationship'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentee', to='mentorships.UserUniversity'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='mentorships.UserUniversity'),
        ),
        migrations.AlterUniqueTogether(
            name='userrole',
            unique_together=set([('role', 'relationship')]),
        ),
    ]
