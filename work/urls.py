from django.conf.urls import url
from . import views as app_views


urlpatterns = [
	url(r'^$', app_views.work, name='work'),
	url(r'^project/(?P<project_slug>[-\w]+)/$',
		app_views.project_detail,
		name='project_detail'),
]