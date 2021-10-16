from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_post', 'description']

admin.site.register(Blog, BlogAdmin)