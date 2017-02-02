from django.conf.urls import url,include,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render
from designers.models import Designers
from designers.forms import SendMail
from django.core.mail import send_mail
from django.conf import settings


def Mail(request):
    email=""
    if request.method == "POST":
        MyRegisterForm = SendMail(request.POST)
        if MyRegisterForm.is_valid():
            Send_To=MyRegisterForm.cleaned_data['Send_To']
            dbuser = Designers.objects.filter(email=Send_To)
            if dbuser:
                user=dbuser[0]
                contact_message =  'your userId and password is {0} {1}'.format(user.designerID,user.password)
                from_email = settings.EMAIL_HOST_USER
                to_email = []
                to_email.append(Send_To)
                send_mail('Registration Succesfull', contact_message, from_email, to_email, fail_silently=False)



        else:
            MyRegisterForm = SendMail(request.GET)

    return render(request, 'designers/SendMails.html',{})



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^designers/',include('designers.urls')),
    url(r'^mail/',  admin.site.admin_view(Mail), name='Mail'),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

