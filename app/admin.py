from .models import Post
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(Post)