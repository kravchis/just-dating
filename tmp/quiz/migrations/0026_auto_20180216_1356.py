# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-16 13:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0025_auto_20180213_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[], verbose_name='Answers'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(unique=True, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(help_text='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(help_text='Alias'),
        ),
        migrations.AlterField(
            model_name='room',
            name='answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[], verbose_name='Answers on the current question'),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='room',
            name='current_question',
            field=models.IntegerField(default=0, verbose_name='Current question number'),
        ),
        migrations.AlterField(
            model_name='room',
            name='current_question_text',
            field=models.TextField(verbose_name='Current question text'),
        ),
        migrations.AlterField(
            model_name='room',
            name='question_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Question time'),
        ),
        migrations.AlterField(
            model_name='room',
            name='questions_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='List of questions indexes'),
        ),
        migrations.AlterField(
            model_name='room',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='Quiz'),
        ),
        migrations.AlterField(
            model_name='room',
            name='token',
            field=models.CharField(db_index=True, help_text='Token', max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('time', 'By time'), ('score', 'By score'), ('end', 'By questions'), ('infinite', 'Infinite')], default='score', max_length=10, verbose_name='Quiz type'),
        ),
        migrations.AlterField(
            model_name='room',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Winner'),
        ),
        migrations.AlterField(
            model_name='roommessage',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='roommessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='roomusers',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='roomusers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(help_text='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='theme',
            name='slug',
            field=models.SlugField(help_text='Alias'),
        ),
    ]