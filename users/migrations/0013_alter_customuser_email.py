# Generated by Django 4.1.7 on 2023-03-31 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_alter_revokedtoken_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email address"),
        ),
    ]
