# Generated by Django 5.1.4 on 2024-12-17 02:56

import employee.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]