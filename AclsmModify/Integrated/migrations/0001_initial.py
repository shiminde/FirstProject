# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authoritys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u6743\u9650', choices=[(b'1', 'Empowerment'), (b'2', 'NoEmpowerment')])),
                ('Auth_name', models.CharField(max_length=64, verbose_name='app', blank=True)),
            ],
            options={
                'verbose_name': '\u6743\u9650\u8868',
                'verbose_name_plural': '\u6743\u9650\u8868',
            },
        ),
        migrations.CreateModel(
            name='Weekly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weeklys', models.CharField(max_length=128, null=True, verbose_name='\u91cd\u70b9\u5de5\u4f5c\u4e8b\u9879', blank=True)),
                ('workplan', models.CharField(max_length=128, null=True, verbose_name='\u5de5\u4f5c\u8ba1\u5212', blank=True)),
                ('completion', models.CharField(max_length=128, null=True, verbose_name='\u672c\u5468\u8ba1\u5212\u5b8c\u6210\u60c5\u51b5', blank=True)),
                ('coordination', models.CharField(max_length=128, null=True, verbose_name='\u5de5\u4f5c\u96be\u70b9\u53ca\u6240\u9700\u534f\u8c03\u7684\u8d44\u6e90', blank=True)),
                ('nextweek', models.CharField(max_length=128, null=True, verbose_name='\u4e0b\u5468\u5de5\u4f5c\u8ba1\u5212', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u8ba1\u5212',
                'verbose_name_plural': '\u5de5\u4f5c\u8ba1\u5212',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(max_length=255, unique=True, serialize=False, verbose_name='\u90ae\u7bb1', primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(default=None, max_length=128, null=True, verbose_name='token', blank=True)),
                ('department', models.CharField(default=None, max_length=32, null=True, verbose_name='\u90e8\u95e8', blank=True)),
                ('tel', models.CharField(default=None, max_length=32, null=True, verbose_name='\u5ea7\u673a', blank=True)),
                ('mobile', models.CharField(default=None, max_length=32, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('memo', models.TextField(default=None, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_end_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f\u8868',
            },
        ),
        migrations.AddField(
            model_name='weekly',
            name='user_name',
            field=models.ForeignKey(verbose_name='\u7528\u6237\u540d', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='authoritys',
            name='user_name',
            field=models.ForeignKey(verbose_name='\u7528\u6237\u540d', to=settings.AUTH_USER_MODEL),
        ),
    ]
