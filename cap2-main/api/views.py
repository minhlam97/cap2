from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.core.files import File
from django.contrib.auth import authenticate

from deepface import DeepFace
# import matplotlib.pyplot as plt
import cv2
import base64
from argparse import Namespace

from api.models import *

from .serializers import List_Song_Serializer,List_SongMood_Serializer,Song_love_Serializer,Play_list_Serializer,Play_list_add_Serializer,Late_song_Serializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.http import HttpResponse
from rest_framework import generics
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

@api_view(['POST'])
def login_api(request):
    try:
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        __,token = AuthToken.objects.create(user)


        message = {'Login information':'Logged in successfully !','id':user.id,'email':user.email,'username':user.username,'token':token,}
        return Response(message,status=status.HTTP_200_OK)
    except:
        message = {'Error message': 'Thông tin đăng nhập không chính xác !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sign_api(request):
    try:
        username = request.data['username_dk']
        password = request.data['password_dk']
        email = request.data['email_dk']

        User.objects.create(email=email,username=username,password=password)
        data_user = User.objects.get(email=email,username=username)
        pw = data_user.password
        data_user.set_password(pw)
        data_user.save()

        message = {'Signup information':'Signup in successfully !','username':username}
        return Response(message,status=status.HTTP_200_OK)
    except:
        message = {'Error message': 'Thông tin đăng kí không chính xác !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_song_love(request):

    name = request.data['name']
    artist = request.data['artist']
    duration = request.data['duration']
    poster = request.data['poster']
    mp3_file = request.data['mp3_file']
    id_Song = request.data['id_Song']
    User_Link = request.data['User_Link']

    data_user = User.objects.get(username=User_Link)

    Song_love.objects.create(name =name ,artist=artist,duration=duration,poster=poster,mp3_file=mp3_file,id_Song=id_Song,User_Link=data_user)

    message = {'Add_song_love information':'Add_song_love in successfully !','name_song':name}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_song_love(request):

    get_song_love = Song_love.objects.all()
    get_song_love_serializer = Song_love_Serializer(get_song_love,many=True)

    message = {'Add_song_love information':'Add_song_love in successfully !','data':get_song_love_serializer.data}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_song_love(request):

    name = request.data['name']
    delete_song_love = Song_love.objects.get(name=name).delete()

    message = {'Delete_song_love information':'Delete_song_love in successfully !'}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def set_play_list(request):
    name_user = request.data['name_user']
    data_user = User.objects.get(username=name_user)
    name = request.data['name']

    Play_list.objects.create(name=name,User_Link=data_user)

    message = {'Set_play_list information':'Set_play_list in successfully !'}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_play_list(request):
    name_user = request.data['name_user']
    data_user = User.objects.get(username=name_user)
    name = request.data['name']

    delete_play_list = Play_list.objects.get(pk=name,User_Link=data_user).delete()

    message = {'Delete_play_list information':'Delete_play_list in successfully !'}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def add_song_play_list(request):

    name = request.data['name']
    artist = request.data['artist']
    duration = request.data['duration']
    poster = request.data['poster']
    mp3_file = request.data['mp3_file']
    id_Song = request.data['id_Song']
    Play_list_Link = request.data['Play_list_Link']

    data_Play_list = Play_list.objects.get(pk=Play_list_Link)

    sss = Play_list_add.objects.filter(name =name,Play_list_Link=data_Play_list)
    sss_serializer = Play_list_add_Serializer(sss,many=True)
    sss_data = sss_serializer.data

    if sss_data == []:

        Play_list_add.objects.create(name =name ,artist=artist,duration=duration,poster=poster,mp3_file=mp3_file,id_Song=id_Song,Play_list_Link=data_Play_list)

    message = {'Add_song_play_list information':'Add_song_play_list in successfully !'}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def get_song_play_list(request):

    name_user = request.data['name_user']
    data_user = User.objects.get(username=name_user)

    get_song_play_list = Play_list.objects.filter(User_Link=data_user)
    get_song_play_list_serializer = Play_list_Serializer(get_song_play_list,many=True)

    message = {'Get_song_play_list information':'Get_song_play_list in successfully !','data':get_song_play_list_serializer.data}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_song_play_list(request):
    pk = request.data['pk']

    delete_play_list_add = Play_list_add.objects.get(pk=pk).delete()

    message = {'Delete_play_list_add information':'Delete_play_list_add in successfully !'}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['POST'])
def add_late_song(request):

    get_late_song = Late_song.objects.all()
    get_late_song_serializer = Late_song_Serializer(get_late_song,many=True)

    name = request.data['name']
    artist = request.data['artist']
    duration = request.data['duration']
    poster = request.data['poster']
    mp3_file = request.data['mp3_file']
    id_Song = request.data['id_Song']
    User_Link = request.data['User_Link']

    DK=0
    for i in get_late_song_serializer.data:
        if i['name'] == name:
            DK=1

    if DK==0 or get_late_song_serializer.data==[] :
        data_user = User.objects.get(username=User_Link)

        Late_song.objects.create(name =name ,artist=artist,duration=duration,poster=poster,mp3_file=mp3_file,id_Song=id_Song,User_Link=data_user)

    message = {'Add_late_song information':'Add_late_song in successfully !'}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_late_song(request):

    get_late_song = Late_song.objects.all()
    get_late_song_serializer = Late_song_Serializer(get_late_song,many=True)

    message = {'Add_song_love information':'Add_song_love in successfully !','data':get_late_song_serializer.data}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_song_moods(request):
    # category = 
    list_song_moods = SongMood.objects.all()
    list_song_moods_serializer = List_SongMood_Serializer(list_song_moods,many=True)
    data_list_song_moods = list_song_moods_serializer.data

    message = data_list_song_moods
    return Response(message,status=status.HTTP_200_OK)


class search_song(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = List_Song_Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','artist']


@api_view(['POST'])
def Scan_Feeling(request):
    # try:
        image_data = request.data['Image_Base64']
        image_data = base64.b64decode(image_data)
        file_name = "mood_image.jpg"
        with open(file_name, 'wb') as f:
                    f.write(image_data)

        objs = DeepFace.analyze(img_path = file_name,actions = ['emotion'])

        data=''

        if objs[0]['dominant_emotion'] == 'happy':
            data = 'Happy'
        if objs[0]['dominant_emotion'] == 'angry':
            data = 'Angry'
        if objs[0]['dominant_emotion'] == 'disgust':
            data = 'Disgust'
        if objs[0]['dominant_emotion'] == 'fear':
            data = 'Fear'
        if objs[0]['dominant_emotion'] == 'surprise':
            data = 'Surprise'
        if objs[0]['dominant_emotion'] == 'sad': 
            data = 'Sad'
        if objs[0]['dominant_emotion'] == 'neutral':
            data = 'Neutral'

        list_song_moods = SongMood.objects.all()
        list_song_moods_serializer = List_SongMood_Serializer(list_song_moods,many=True)
        data_list_song_moods = list_song_moods_serializer.data

        for i in data_list_song_moods:
            if i['mood'] == data:
               List_Song = i['songs'] 

        message = {'Thong bao':'Thanh cong','Data':data,'List_Song':List_Song}
        return Response(message,status=status.HTTP_200_OK)
    # except:
    #     message = {'Thong bao':'Thửi lại với 1 bức ảnh khác'}
    #     return Response(message, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def Get_Song_Love(request):
#     Song_love.objects.create(name=email,artist=username,duration=password,poster=True,mp3_file,User_Link=)

#     message = data_list_song_moods
#     return Response(message,status=status.HTTP_200_OK)