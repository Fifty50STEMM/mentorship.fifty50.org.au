# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-08 06:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('order_in_year', models.PositiveSmallIntegerField(verbose_name='Order in Year')),
                ('reference', models.CharField(help_text="Human readable version of session, eg 'Semester 1, 2018'", max_length=255, verbose_name='Reference')),
                ('abbreviation', models.CharField(blank=True, max_length=32, unique=True, verbose_name='Abbreviation')),
            ],
        ),
        migrations.CreateModel(
            name='SessionWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=3, unique=True, verbose_name='Week (number)')),
                ('description', models.CharField(max_length=255, verbose_name='Full Name')),
                ('information', models.TextField(blank=True, verbose_name='Information')),
            ],
        ),
        migrations.CreateModel(
            name='UniversitySession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_id', models.CharField(max_length=64, unique=True)),
                ('why_mentor', models.CharField(max_length=150, null=True, verbose_name='Why do you want to become a mentor?')),
                ('why_diversity', models.CharField(max_length=150, null=True, verbose_name='Why do you think diversity, equity and inclusion in STEM are important?')),
                ('hear_about', models.CharField(max_length=150, null=True, verbose_name='How did you hear about this program?')),
                ('mentee_number', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('gender_mode', models.CharField(blank=True, choices=[('strict', 'Important to me*'), ('optional', 'If possible'), ('na', 'Not important to me')], max_length=1, verbose_name='Gender Mode')),
                ('method_preferences', models.ManyToManyField(to='universities.Method')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.University')),
            ],
            options={
                'verbose_name_plural': 'university users',
            },
        ),
    ]
