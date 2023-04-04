from rest_framework import serializers,validators
from django.contrib.auth.models import User
from api.models import SongMood,Song,User,UserFollowing
from rest_framework.validators import ValidationError

import random
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status

class List_Song_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'

class List_SongMood_Serializer(serializers.ModelSerializer):
    songs = List_Song_Serializer(many=True,read_only=True)
    class Meta:
        model=SongMood
        fields='__all__'