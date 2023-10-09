# Generated by Django 4.2 on 2023-10-09 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('identifier_system', models.URLField()),
                ('identifier_value', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[1-9][0-9]*$')])),
                ('patient', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[1-9][0-9]{9}$')])),
                ('practitioner', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[1-9][0-9]{9}$')])),
                ('organization', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[1-9][0-9]{9}$')])),
            ],
        ),
    ]
