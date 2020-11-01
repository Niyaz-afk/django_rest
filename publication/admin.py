from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Публикации"""
    list_display = ('id','title', 'date')


admin.site.site_title = 'Блог'
admin.site.site_header = 'Блог'
