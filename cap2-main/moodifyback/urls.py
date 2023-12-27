"""moodifyback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from api import views

from rest_framework.routers import DefaultRouter,SimpleRouter
from api import views

# router = DefaultRouter()
# router.register('api/seach_song',views.seach_song)

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),

    path('Scan_Feeling',views.Scan_Feeling),
    path('login_api',views.login_api),
    path('sign_api',views.sign_api),
    path('add_song_love',views.add_song_love),
    path('get_song_love',views.get_song_love),
    path('delete_song_love',views.delete_song_love),
    path('set_play_list',views.set_play_list),
    path('get_song_play_list',views.get_song_play_list),
    path('delete_play_list',views.delete_play_list),
    path('add_song_play_list',views.add_song_play_list),
    path('add_late_song',views.add_late_song),
    path('get_late_song',views.get_late_song),
    path('delete_song_play_list',views.delete_song_play_list),

    # path('', include(router.urls)),

  
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
