# Generated by Django 4.2.4 on 2023-09-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0007_alter_playerteam_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerteam",
            name="time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
