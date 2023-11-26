from django.db import models

# Create your models here.
class Seism(models.Model):

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    magnitude = models.IntegerField()
    depth = models.IntegerField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()