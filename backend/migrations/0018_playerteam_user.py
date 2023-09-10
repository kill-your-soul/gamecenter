# Generated by Django 4.2.4 on 2023-09-10 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("backend", "0017_alter_playerteam_options_alter_playerteam_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="playerteam",
            name="user",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]