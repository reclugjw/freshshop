# Generated by Django 2.0.2 on 2020-06-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级')], help_text='级别', verbose_name='级别'),
        ),
    ]
