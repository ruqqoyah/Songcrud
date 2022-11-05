from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Age = models.PositiveSmallIntegerField()

    def __str__(self):
        return (str(self.first_name) + ' ' + str(self.last_name))

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.today)
    likes = models.PositiveIntegerField()
    artiste_id = models.IntegerField()

    def __str__(self):
        return (str(self.title))


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(max_length=3500)
    song_id = models.IntegerField()

    def __str__(self):
        return (str(self.Song))
