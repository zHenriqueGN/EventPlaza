from django.db import models
from core.apps.authentication.models import User

# Create your models here.


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="events_logos")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    participants = models.ManyToManyField(User, "event_participants")

    def __str__(self):
        return self.title
