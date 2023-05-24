from django.urls import path
from api import views


urlpatterns = [
    path('', views.index, name='index'),
    path("list_song_moods",views.list_song_moods),
    path('search_song', views.search_song.as_view()),
]
