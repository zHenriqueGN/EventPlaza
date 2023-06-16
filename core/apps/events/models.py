from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="event_logos")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
