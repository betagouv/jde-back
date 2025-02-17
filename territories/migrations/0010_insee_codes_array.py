# Generated by Django 4.2.17 on 2025-02-03 08:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("territories", "0009_city_nb_students"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="city",
            name="insee_code",
        ),
        migrations.AddField(
            model_name="city",
            name="insee_codes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=5), default=list, size=None
            ),
        ),
    ]
