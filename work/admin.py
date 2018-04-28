from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Project, Feedback


class ProjectAdmin(MarkdownxModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Feedback)
