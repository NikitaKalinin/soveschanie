from django.db import models

# Create your models here.
class Room(models.Model):
    proctor_id = models.CharField(max_length=50, default='proctor')
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.description)
