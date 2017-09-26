from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^/new$', views.show_add_user),
    url(r'^/create$', views.create),
    url(r'^/(?P<id>\d+)$', views.show),
    url(r'^/edit$', views.edit_page),
    url(r'^/(?P<id>\d+)/edit$', views.edit_page),
    url(r'^/process_edit$', views.update),
     url(r'^/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^/$', views.index),     # This line has changed!

    
    
]