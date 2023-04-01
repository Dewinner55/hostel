# Generated by Django 4.1.7 on 2023-03-29 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Apartment", "0001_initial"),
        ("ApartmentsRating", "0006_apartmentsrating_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartmentsrating",
            name="apartment",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Apartment.apartment",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsrating",
            name="user",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
