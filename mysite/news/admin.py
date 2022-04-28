from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'created_at', 'updated_at', 'is_published', )
    list_display_links = ('id', "title", "email",)
    search_fields = ('title', 'content')




admin.site.register(News, NewsAdmin)