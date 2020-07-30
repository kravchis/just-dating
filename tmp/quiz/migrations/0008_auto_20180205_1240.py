# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20180205_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='token',
            field=models.CharField(default='', help_text='\u0422\u043e\u043a\u0435\u043d', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='lang',
            field=models.CharField(default='ru', help_text='Language', max_length=2),
        ),
    ]