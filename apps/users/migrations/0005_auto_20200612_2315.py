# Generated by Django 2.0.2 on 2020-06-12 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200612_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=7, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 23, 15, 24, 950129), verbose_name='添加时间'),
        ),
    ]