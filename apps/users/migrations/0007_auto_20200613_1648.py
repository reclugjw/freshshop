# Generated by Django 2.0.2 on 2020-06-13 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200613_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 16, 48, 5, 272726), verbose_name='添加时间'),
        ),
    ]