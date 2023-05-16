from django.db import models
from django.contrib.auth.models import User

class Map_object(models.Model):
    name = models.CharField(max_length=80)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
# user: what user created it?
# places: all places in it.
# public: is it public?
class RoadTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    places = models.ManyToManyField(Map_object)
    is_public = models.BooleanField(default=False)
