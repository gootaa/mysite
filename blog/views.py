from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
	"""
	Standard list view
	"""
	posts = Post.published.all()

	return render(request, 'post_list.html', {'posts':posts})


def post_detail(request, post_slug):
	"""
	Standard detail view
	"""
	post = get_object_or_404(Post, slug=post_slug, status='published')

	return render(request, 'post_detail.html', {'post':post})
