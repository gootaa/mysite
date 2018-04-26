from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
	"""
	A manger for published posts only
	"""
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
	"""
	Represents a standard time stamped
	blog post.
	"""
	STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published')
    )

	created = models.DateTimeField(auto_add_now=True)
	updated = models.DateTimeField(auto_add=True)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	pic = models.ImageField(upload_to='posts/')
	body = MarkdownxField()
	status = models.CharField(max_length=10,
							  choices=STATUS_CHOICES,
							  default='draft')

	objects = models.Manager()
	published = PublishedManager()

	class Meta:
		ordering = ('-updated')

	@property 
    def formatted_markdown(self):  # This will be used in templates
        return markdownify(self.content)

    def get_absolute_url(self):
    	return reverse('post_detail', args=(self.slug,))

    def __str__(self):
    	return self.title


