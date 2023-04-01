# Generated by Django 4.1.7 on 2023-03-30 06:20

import Apartment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Apartment", "0002_apartment_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name="apartment",
            name="address",
            field=models.CharField(
                max_length=200,
            ),
        ),
    ]
