# Generated by Django 4.1.3 on 2022-11-23 13:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("type", models.CharField(max_length=20)),
                ("date", models.CharField(max_length=20)),
                ("value", models.CharField(max_length=20)),
                ("cpf", models.CharField(max_length=20)),
                ("card", models.CharField(max_length=20)),
                ("hour", models.CharField(max_length=20)),
                ("shop_owner", models.CharField(max_length=20)),
                ("shop_name", models.CharField(max_length=20)),
            ],
        ),
    ]