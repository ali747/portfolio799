# Generated by Django 4.1 on 2022-08-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefcase', '0003_alter_bio_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='city',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]
