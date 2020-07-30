# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 16:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0019_room_current_question_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_right', models.BooleanField(default=False)),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Question')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Room', verbose_name='Room')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
        ),
    ]