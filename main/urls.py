from django.conf.urls import url
from . import views

# namespaceing
app_name = 'main'

urlpatterns = [
	#/main/
	url(r'^$', views.index, name='index'),
	# /main/search/
	url(r'^search/$', views.search, name='search'),
]
