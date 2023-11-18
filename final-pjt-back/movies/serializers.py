from rest_framework import serializers
from .models import Movie,Genre, Score, Actor, Director




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'
        read_only_fields= ('movie', 'user',)

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        # read_only_fields=('movie',)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields ='__all__'


