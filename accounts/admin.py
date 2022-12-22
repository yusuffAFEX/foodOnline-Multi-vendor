from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active']
    list_display_links = ['username', 'email']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('-date_joined',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
