# Generated by Django 4.2.2 on 2023-06-23 19:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0003_alter_event_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                related_name="event_participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
