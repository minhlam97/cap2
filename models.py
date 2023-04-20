from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Meta:
        ordering = ["id"]
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').null = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('username').null = False
    AbstractUser._meta.get_field('password').blank = False
    AbstractUser._meta.get_field('password').null = False
    # Money = models.IntegerField(default = 0,null=False)
    # Total_recharge_money = models.IntegerField(default = 0,null=True, blank=True)
    # Total_amount_deducted = models.IntegerField(default = 0,null=True, blank=True)
    # Avatar = models.ImageField(upload_to='upload/User',null=True,blank=True)
    # OTP = models.CharField(max_length=10, null=True, blank=True)
    # Two_factor_authentication = models.CharField(max_length=200, null=True, blank=True,default='OFF')
    # Password_Level_2 = models.CharField(max_length=10, null=True, blank=True)


class SongMood(models.Model):

    MOOD_CHOICES = (
        ("Happy", "Happy"),
        ("Sad", "Sad"),
        ("Angry", "Angry"),
        ("Surprise", "Surprised"),
        ("Neutral", "Neutral"),
        ("Disgust","Disgust"),
        ("Fear","Fear")
    )


    mood = models.CharField(choices=MOOD_CHOICES, max_length=50)

    def __str__(self):

        return self.mood

# class UserFollowing(models.Model):
    
#     user_id = models.ForeignKey(to=User, related_name="following", on_delete=models.CASCADE, blank=True, null=True)
#     following_user_id = models.ForeignKey(to=User, related_name="followers", on_delete=models.CASCADE, blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)

class Song(models.Model):

    name = models.CharField(max_length=150,blank=True, null=True,unique=True)
    artist = models.CharField(max_length=150, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    poster = models.ImageField(upload_to="song_posters", blank=True, null=True)
    mp3_file = models.FileField(upload_to="song_files", blank=True, null=True)
    love = models.CharField(max_length=150,default='love')
    mood = models.ManyToManyField(to=SongMood, related_name="songs", blank=True, null=True)

    def __str__(self):
        return self.name

class Song_love(models.Model):

    name = models.CharField(max_length=150, blank=True, null=True,unique=True)
    artist = models.CharField(max_length=150, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    poster = models.CharField(max_length=350, blank=True, null=True)
    mp3_file = models.CharField(max_length=350, blank=True, null=True)
    id_Song = models.CharField(max_length=150, blank=True, null=True)
    User_Link = models.ForeignKey('User',related_name='User_Link_Song_love',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Play_list(models.Model):

    name = models.CharField(max_length=150, blank=True, null=True)
    User_Link = models.ForeignKey('User',related_name='User_Link_Play_list',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Play_list_add(models.Model):

    name = models.CharField(max_length=150, blank=True, null=True)
    artist = models.CharField(max_length=150, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    poster = models.CharField(max_length=350, blank=True, null=True)
    mp3_file = models.CharField(max_length=350, blank=True, null=True)
    id_Song = models.CharField(max_length=150, blank=True, null=True)
    Play_list_Link = models.ForeignKey('Play_list',related_name='Play_list_Link',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Late_song(models.Model):
    
    name = models.CharField(max_length=150, blank=True, null=True)
    artist = models.CharField(max_length=150, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    poster = models.CharField(max_length=350, blank=True, null=True)
    mp3_file = models.CharField(max_length=350, blank=True, null=True)
    id_Song = models.CharField(max_length=150, blank=True, null=True)
    User_Link = models.ForeignKey('User',related_name='User_Link_Late_song',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name