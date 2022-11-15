# Generated by Django 4.0.6 on 2022-07-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=65, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deadline_at", models.DateTimeField(blank=True, null=True)),
                ("completed", models.BooleanField()),
                (
                    "tags",
                    models.ManyToManyField(
                        related_name="tags", to="tasks.tag"
                    ),
                ),
            ],
            options={
                "ordering": ["completed", "-created_at"],
            },
        ),
    ]
