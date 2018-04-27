from django.conf.urls import url, include
from . import views as app_views


urlpatterns = [
	url(r'^$', app_views.post_list, name='post_list'),
	url(r'^(?P<post_slug>[-\w]+)/$', app_views.post_detail, name='post_detail'),
]