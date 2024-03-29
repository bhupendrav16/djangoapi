# Generated by Django 5.0.1 on 2024-01-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("location", models.TextField()),
                (
                    "domain",
                    models.CharField(
                        choices=[("IT", "IT"), ("Non IT", "Non IT")], max_length=40
                    ),
                ),
            ],
        ),
    ]
