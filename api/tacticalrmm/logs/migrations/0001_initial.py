# Generated by Django 3.0.6 on 2020-05-18 07:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PendingAction",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entry_time", models.DateTimeField(auto_now_add=True)),
                (
                    "action_type",
                    models.CharField(
                        blank=True,
                        choices=[("schedreboot", "Scheduled Reboot")],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("completed", "Completed")],
                        default="pending",
                        max_length=255,
                    ),
                ),
                ("celery_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "details",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True
                    ),
                ),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pendingactions",
                        to="agents.Agent",
                    ),
                ),
            ],
        ),
    ]
