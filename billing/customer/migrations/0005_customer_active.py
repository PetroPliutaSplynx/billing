# Generated by Django 3.1 on 2020-09-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200917_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
