from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .  models import Designers
from . forms import DesignerDetails
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
# Create your views here.

def index(request):
    if request.session.has_key('designerID'):
        designerID = request.session['designerID']
        dbuser = Designers.objects.filter(designerID=designerID)
        user = dbuser[0]
        profilepic = user.profilepic.url
        return render(request, 'designers/loggedin.html', {"designerID": designerID, 'profilepic': profilepic})
    context={

    }
    return render(request,'designers/index.html',context=context)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registeration(request):
    designerID=""

    password=""
    if request.method == "POST":
        if request.session.has_key('designerID'):
            designerID = request.session['designerID']
            dbuser = Designers.objects.filter(designerID=designerID)
            user = dbuser[0]
            profilepic = user.design.url
            return render(request, 'designers/loggedin.html', {"designerID": designerID,'profilepic':profilepic})
        # Get the posted form
        MyRegisterForm = DesignerDetails(request.POST)
        content={'form':MyRegisterForm}
        print( MyRegisterForm.errors)
        if MyRegisterForm.is_valid():
            designerID=MyRegisterForm.cleaned_data['designerID']

            password=MyRegisterForm.cleaned_data['password']

            print(designerID)
            dbuser = Designers.objects.filter(designerID=designerID,password=password)
            user=dbuser[0]
            profilepic=user.profilepic.url
            content={
                'designerID': designerID,

            }
            if not dbuser:
                print("Not user")
                return render(request, 'designers/register.html', {})


            else:
                print(dbuser)
                request.session['designerID'] = designerID

                return render(request,'designers/loggedin.html',{'designerID':designerID,'profilepic':profilepic})

        else:
            print("not valid")
            return render(request, 'designers/register.html', {})
    else:
       MyRegisterForm=DesignerDetails(request.GET)
       if request.session.has_key('designerID'):
           designerID = request.session['designerID']
           dbuser = Designers.objects.filter(designerID=designerID)
           user = dbuser[0]
           profilepic = user.design.url
           return render(request, 'designers/loggedin.html', {"designerID": designerID, 'profilepic': profilepic})
       return render(request, 'designers/register.html', {})

class DesignerCreate(CreateView):
    model=Designers
    fields = ['name','firmname','contact','address','profilepic','email','design1','design2','design3']
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    try:
      del request.session['designerID']
    except:
      pass
    return HttpResponse("<strong>You are logged out.</strong>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):

    if request.session.has_key('designerID'):
        designerID = request.session['designerID']
        dbuser = Designers.objects.filter(designerID=designerID)
        user = dbuser[0]
        profilepic = user.profilepic.url
        print(profilepic)
        return render(request, 'designers/loggedin.html', {"designerID": designerID,'profilepic':profilepic})
    return  render(request,'designers/register.html',{})