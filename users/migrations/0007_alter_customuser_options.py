# Generated by Django 4.1.7 on 2023-03-28 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_customuser_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
