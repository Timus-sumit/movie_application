# Generated by Django 3.0.5 on 2020-04-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0010_auto_20200412_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='pub_date',
            field=models.DateTimeField(default='1/1/20'),
        ),
    ]
