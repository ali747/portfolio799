# Generated by Django 4.1 on 2022-08-29 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefcase', '0009_alter_employeeskills_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_strength',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.DeleteModel(
            name='EmployeeSkills',
        ),
    ]
