# Generated by Django 4.2.4 on 2023-09-10 19:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0018_playerteam_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="curator",
            name="name",
        ),
        migrations.RemoveField(
            model_name="curator",
            name="password",
        ),
        migrations.RemoveField(
            model_name="playerteam",
            name="password",
        ),
        migrations.RemoveField(
            model_name="playerteam",
            name="teamname",
        ),
    ]
