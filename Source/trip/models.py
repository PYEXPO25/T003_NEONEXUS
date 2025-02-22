from django.db import models # type: ignore

class HiddenSpot(models.Model):

    destination = models.CharField(max_length=200)

    selected_spots = models.TextField()  # Store selected spots as JSON or CSV

    def __str__(self):

        return self.destination + " " + self.selected_spots   
# Create your models here.
