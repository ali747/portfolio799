# Generated by Django 4.1 on 2022-09-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefcase', '0011_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(),
        ),
    ]