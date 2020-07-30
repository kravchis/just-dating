# Generated by Django 3.0.7 on 2020-07-29 06:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('quiz', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Alias')),
                ('name', models.CharField(help_text='Name', max_length=100)),
                ('questions', models.ManyToManyField(to='quiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('questionend', 'Till questions are fineshed.'), ('infinite', 'Infinite quize (looping over questions).'), ('custom', 'Custom. Defining question by author.')], default='questionend', max_length=50, verbose_name='Quiz type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('question_time', models.DateTimeField(auto_now_add=True, verbose_name='Question time')),
                ('current_question', models.IntegerField(default=0, verbose_name='Current question number')),
                ('current_question_text', models.TextField(verbose_name='Current question text')),
                ('answers', models.CharField(default='', help_text='Divided by coma', max_length=250, verbose_name='Answers')),
                ('questions_json', django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='List of questions indexes')),
                ('is_done', models.BooleanField(default=False)),
                ('token', models.CharField(db_index=True, help_text='Token', max_length=100)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='Quiz')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.UserProfile', verbose_name='Winner')),
            ],
        ),
        migrations.CreateModel(
            name='RoomUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='Score')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Room', verbose_name='Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='RoomQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Question')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Room', verbose_name='Room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_right', models.BooleanField(default=False)),
                ('is_service', models.BooleanField(default=False)),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Question')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Room', verbose_name='Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile', verbose_name='User')),
            ],
        ),
    ]