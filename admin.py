from django.contrib import admin
from api.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('id','email', 'username')
    search_fields = ('email', 'username')

    # fieldsets = BaseUserAdmin.fieldsets
    # fieldsets[0][1]['fields'] = fieldsets[0][1]['fields'] + (
    #     'Money','Total_recharge_money','Total_amount_deducted','Avatar','OTP','Two_factor_authentication'
    # )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email','username', 'password1', 'password2','Avatar')}
    #     ),
    # )
admin.site.register(User,UserAdmin)

class Song_love_Admin(admin.ModelAdmin):
	list_display = ('id','name','artist','duration','User_Link')
	search_fields = ('name','artist','duration','User_Link',)

admin.site.register(Song_love,Song_love_Admin)

class Play_list_Admin(admin.ModelAdmin):
    list_display = ('id','name','User_Link')
    search_fields = ('name',)

admin.site.register(Play_list,Play_list_Admin)

class Play_list_add_Admin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)

admin.site.register(Play_list_add,Play_list_add_Admin)

class Late_song_Admin(admin.ModelAdmin):
    list_display = ('id','name','User_Link')
    search_fields = ('name',)

admin.site.register(Late_song,Late_song_Admin)

admin.site.register(Song)
admin.site.register(SongMood)

