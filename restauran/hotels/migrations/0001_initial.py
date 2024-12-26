# Generated by Django 5.1.3 on 2024-12-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="hotel_images/")),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (2, "2 yulduzli"),
                            (3, "3 yulduzli"),
                            (4, "4 yulduzli"),
                            (5, "5 yulduzli"),
                        ]
                    ),
                ),
                ("is_open_now", models.BooleanField(default=True)),
                ("working_hours", models.CharField(max_length=50)),
                ("address", models.TextField()),
                ("phone", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]