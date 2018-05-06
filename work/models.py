from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.core.urlresolvers import reverse


class Project(models.Model):
    """
    Represents a model for 
    my personal projects
    """
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    pic = models.ImageField(upload_to='projects/')
    description = MarkdownxField()

    @property 
    def formatted_markdown(self):# This will be used in templates
        return markdownify(self.description)

    def get_absolute_url(self):
        return reverse('project_detail', args=(self.slug,))

    def __str__(self):
        return self.name


class Feedback(models.Model):
    """
    Represents client feedback
    """
    client_name = models.CharField(max_length=250)
    client_pic = models.ImageField(upload_to='clients/', blank=True)
    client_link = models.URLField()
    quote = models.TextField()

    def __str__(self):
        return self.client_name
