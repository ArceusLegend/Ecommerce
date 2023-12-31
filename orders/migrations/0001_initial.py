# Generated by Django 4.2.4 on 2023-08-19 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=50)),
                ("address1", models.CharField(max_length=250)),
                ("address2", models.CharField(max_length=250)),
                ("city", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("post_code", models.CharField(max_length=20)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("total_paid", models.DecimalField(decimal_places=2, max_digits=5)),
                ("order_key", models.CharField(max_length=200)),
                ("billing_status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="order_user", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
