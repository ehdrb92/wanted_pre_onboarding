from django.contrib import admin
from .models import User, Company

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']

@admin.register(Company)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']