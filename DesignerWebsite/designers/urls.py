from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'add/$',views.DesignerCreate.as_view(),name='register'),
    url(r'login/$',TemplateView.as_view(template_name='designers/register.html')),
    url(r'registeration/$', views.registeration , name='registeration'),
]
