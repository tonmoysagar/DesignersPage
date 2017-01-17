from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'register/$',views.DesignerCreate.as_view(),name='register'),
    url(r'login/$',views.login,name='login'),
    url(r'dashboard/$', views.registeration , name='registeration'),
    url(r'^logout/$', views.logout, name = 'logout'),
]
