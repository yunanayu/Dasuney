from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    id = models.IntegerField()  # movie_id
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()


# class Credit(models.Model):
#     movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
#     actor1 = models.CharField(max_length=30)
#     actor2 = models.CharField(max_length=30)
#     actor3 = models.CharField(max_length=30)
#     actor4 = models.CharField(max_length=30)
#     actor5 = models.CharField(max_length=30)
#     actor6 = models.CharField(max_length=30)
    
class Actor(models.Model):
    movie = models.ManyToManyField(Movie)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='actor_like')


class Director(models.Model):
    director = models.CharField(max_length=30)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)