# Generated by Django 3.1 on 2020-09-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_transaction_system'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
