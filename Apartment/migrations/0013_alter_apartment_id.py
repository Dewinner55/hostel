# Generated by Django 4.1.7 on 2023-03-31 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Apartment", "0012_alter_apartment_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartment",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
