# Generated by Django 3.0.5 on 2020-04-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20200411_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='pub_date',
            field=models.DateTimeField(default=True),
        ),
    ]