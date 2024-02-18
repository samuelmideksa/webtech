from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.genre

class Artist(models.Model):
    artist = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.artist


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()
    album_art = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return self.name
    
    def genre_list(self):
        return list(self.genre.values_list('genre', flat=True))
