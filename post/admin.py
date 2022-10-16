from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'country', 'region', 'position', 'compensation', 'skill', 'context']
    list_display_links = ['id']