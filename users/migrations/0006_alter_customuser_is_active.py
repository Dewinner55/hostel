# Generated by Django 4.1.7 on 2023-03-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_revokedtoken_timestamp_revokedtoken_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
