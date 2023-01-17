# Generated by Django 4.1.5 on 2023-01-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ratings', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('timing', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150, unique=True)),
                ('url', models.URLField()),
                ('services', models.CharField(choices=[('Coffee', 'Coffee'), ('Food', 'Food'), ('Veggies', 'Veggies'), ('Alcohol', 'Alcohol'), ('Cards', 'Cards')], max_length=150)),
                ('tables', models.IntegerField()),
                ('wifi', models.BooleanField()),
                ('sockets', models.IntegerField()),
                ('long_stays', models.BooleanField()),
                ('quiet', models.BooleanField()),
                ('calls', models.BooleanField()),
            ],
        ),
    ]
