from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','followings',)
        
class FollowSerializer(serializers.ModelSerializer):
    
    followers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        # include = ('id','username','followings','followers',)
        fields = '__all__'