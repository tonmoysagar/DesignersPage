from django.conf.urls import url,include,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def my_view(request):
    return HttpResponse("Hello!")

def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^my_view/$', admin.site.admin_view(my_view))
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^designers/',include('designers.urls')),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

