# Generated by Django 4.2.4 on 2023-09-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0006_curator_station_playerteam_time_station_points_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerteam",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]