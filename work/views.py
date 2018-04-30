from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Feedback
from .forms import MessageForm
from django.core.mail import send_mail
from django.contrib import messages


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


def contact(request):
	"""
	Displays message form, social media
	links and direct email
	"""
	form = MessageForm()
	return render(request, 'contact.html', {'form':form})


def send_message(request):
	"""
	Sends email with the message
	"""
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			message = '{} says: {}'.format(cd['name'], cd['message'])
			send_mail(
    			cd['subject'],
    			message,
    			cd['email'],
    			['abdullah@goota.me'],
    			fail_silently=False,
			)
			messages.success(request, 'Your message was sent successfully!')
	return redirect('contact')

