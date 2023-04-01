# Generated by Django 4.1.7 on 2023-03-30 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "Apartment",
            "0005_remove_apartment_name_apartment_city_apartment_state_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apartment",
            name="address",
        ),
        migrations.AlterField(
            model_name="apartment",
            name="city",
            field=models.CharField(blank=True, max_length=100, verbose_name="Город"),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="state",
            field=models.CharField(max_length=100, verbose_name="Округ"),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="street",
            field=models.CharField(blank=True, max_length=200, verbose_name="Улица"),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
