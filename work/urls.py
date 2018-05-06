from django.conf.urls import url
from . import views as app_views


urlpatterns = [
	url(r'^$', app_views.work, name='work'),
	url(r'^project/(?P<project_slug>[-\w]+)/$',
		app_views.project_detail,
		name='project_detail'),
	url(r'^contact/$', app_views.contact, name='contact'),
	url(r'^send-message/$', app_views.send_message, name='send_message'),
]