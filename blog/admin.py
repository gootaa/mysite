from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(MarkdownxModelAdmin):
	list_view = ('title', 'status', 'slug',)
	list_filter = ('status', 'created', 'updated',)
	search_fields = ('title', 'body',)
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'updated'
	ordering = ['status', '-updated']

admin.site.register(Post, PostAdmin)
