from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from managementApp.models import CustomUser


class UserModel(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'user_type')

admin.site.register(CustomUser,UserModel)
