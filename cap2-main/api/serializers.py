from rest_framework import serializers,validators
from api.models import SongMood,Song,Song_love,User,Play_list,Play_list_add,Late_song
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

class Song_love_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Song_love
        fields='__all__'

class Play_list_add_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Play_list_add
        fields='__all__'

class Play_list_Serializer(serializers.ModelSerializer):
    Play_list_Link = Play_list_add_Serializer(many=True,read_only=True)
    class Meta:
        model=Play_list
        fields='__all__'

class Late_song_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Late_song
        fields='__all__'

class User_Serializer(serializers.ModelSerializer):
    User_Link_Song_love = Song_love_Serializer(many=True,read_only=True)
    User_Link_Play_list = Play_list_Serializer(many=True,read_only=True)
    class Meta:
        model=User 
        fields='__all__' 