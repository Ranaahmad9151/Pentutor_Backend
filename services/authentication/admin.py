from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import CustomUser

admin.site.register(CustomUser, UserAdmin)
