# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-08 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='id_text',
            field=models.CharField(max_length=200, null=True, verbose_name='Enter a new identification number'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='What is your ID?'),
        ),
    ]
