# Generated by Django 3.1 on 2020-09-18 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20200918_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mac_address',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
