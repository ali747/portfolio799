# Generated by Django 4.1 on 2022-08-29 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briefcase', '0007_bio_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bio',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='employeeskills',
            options={'ordering': ['employee_id', 'skill_id']},
        ),
        migrations.AlterModelTable(
            name='employeeskills',
            table='briefcase_employeeskills',
        ),
    ]
