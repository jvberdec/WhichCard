# Generated by Django 2.2.7 on 2020-04-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20200411_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='rewardValue',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]