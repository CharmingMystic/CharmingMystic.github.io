from django.db import models
from django.contrib.auth.models import User
from map.models import Map_object


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_items = models.ManyToManyField(Map_object)

    def __str__(self):
        return str(self.user)