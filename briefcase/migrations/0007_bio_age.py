# Generated by Django 4.1 on 2022-08-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefcase', '0006_bio_phone_number_alter_bio_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
