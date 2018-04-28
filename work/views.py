from django.shortcuts import render, get_object_or_404
from .models import Project, Feedback


def work(request):
	"""
	Standard list view for both projects
	and feedbacks
	"""
	feedbacks = Feedback.objects.all()
	projects = Project.objects.all()
	return render(request,
				  'work.html',
				  {'feedbacks':feedbacks,
				   'projects':projects,})


def project_detail(request, project_slug):
	"""
	Standard detail view
	"""
	project = get_object_or_404(Project, slug=project_slug)
	return render(request, 'project_detail.html', {'project':project})
