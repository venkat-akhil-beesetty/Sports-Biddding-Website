# Generated by Django 3.2.1 on 2021-05-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_rename_payment_payme'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payme',
            new_name='payment1',
        ),
    ]