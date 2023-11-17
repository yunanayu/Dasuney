from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_like')
    title = models.CharField(max_length=50)
    movie_id = models.IntegerField()  # movie_id
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)



class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()
     
    class Meta:
        unique_together =('movie', 'user')


class Actor(models.Model):
    movie = models.ManyToManyField(Movie)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='actor_like')
    actor_name = models.CharField(max_length=100)
    actor_id = models.IntegerField()



class Director(models.Model):
    movie = models.ManyToManyField(Movie)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='director_like')
    director_name = models.CharField(max_length=30)
    director_id = models.IntegerField()