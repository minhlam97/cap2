from django.contrib import admin
from api.models import *
from django.db import models

# Register your models here.
# class Music (models.Model):
#     name = models.Charfield(max_length=100)
#     file = models.FileField(upload_to='/music')


admin.site.register(Song)
admin.site.register(SongMood)
admin.site.register(User)
admin.site.register(UserFollowing)
