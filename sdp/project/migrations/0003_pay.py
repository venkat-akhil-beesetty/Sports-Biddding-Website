# Generated by Django 3.2.1 on 2021-05-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Zip', models.BigIntegerField(max_length=50)),
                ('Nameoncard', models.CharField(max_length=50)),
                ('Creditcardnumber', models.BigIntegerField(max_length=50)),
                ('ExpMonth', models.CharField(max_length=50)),
                ('ExpYear', models.BigIntegerField(max_length=50)),
                ('CVV', models.BigIntegerField(max_length=50)),
            ],
        ),
    ]
