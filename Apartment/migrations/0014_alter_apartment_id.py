# Generated by Django 4.1.7 on 2023-03-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Apartment", "0013_alter_apartment_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
