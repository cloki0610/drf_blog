""" Manage Post Model display in admin site """
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Show model in admin table with follow rules """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'publish_on', 'updated_on')
    list_display = ('title', 'author', 'publish_on', 'updated_on')
    search_fields = ['title', 'excerpt']