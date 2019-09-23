from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField(default=0.0)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)

    def __str__(self):
        return '{0}, ({1}) | {2}'.format(self.name, self.release_date, self.genre)
