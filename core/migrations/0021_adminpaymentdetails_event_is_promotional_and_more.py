# Generated by Django 5.1.4 on 2025-03-01 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_notification_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminPaymentDetails",
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
                ("upi_id", models.CharField(max_length=255)),
                ("account_number", models.CharField(max_length=50)),
                ("ifsc_code", models.CharField(max_length=20)),
                ("bank_name", models.CharField(max_length=100)),
                ("account_holder_name", models.CharField(max_length=255)),
                (
                    "promotion_price",
                    models.DecimalField(decimal_places=2, default=50.0, max_digits=10),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="is_promotional",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="event",
            name="promotion_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("payment_pending", "Payment Pending"),
                    ("payment_verification", "Payment Verification"),
                    ("promoted", "Promoted"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="EventPayment",
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
                ("transaction_id", models.CharField(max_length=255)),
                (
                    "payment_screenshot",
                    models.ImageField(upload_to="payment_screenshots/"),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("completed", "Completed"),
                            ("failed", "Failed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "event",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to="core.event",
                    ),
                ),
            ],
        ),
    ]
