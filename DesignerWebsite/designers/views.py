from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .  models import Designers
from . forms import DesignerDetails,PortfolioDetails
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
# Create your views here.

def index(request):
    if request.session.has_key('designerID'):
        designerID = request.session['designerID']
        dbuser = Designers.objects.filter(designerID=designerID)
        if dbuser:
            context = {
                'dbuser': dbuser
            }
            return render(request, 'designers/loggedin.html', context)
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
            if dbuser:
                context = {
                    'dbuser': dbuser
                }


                return render(request, 'designers/loggedin.html', context)
        # Get the posted form
        MyRegisterForm = DesignerDetails(request.POST)
        content={'form':MyRegisterForm}
        print( MyRegisterForm.errors)
        if MyRegisterForm.is_valid():
            designerID=MyRegisterForm.cleaned_data['designerID']

            password=MyRegisterForm.cleaned_data['password']

            print(designerID)
            dbuser = Designers.objects.filter(designerID=designerID,password=password)
            if dbuser:
                user = dbuser[0]
                profilepic = user.profilepic.url
                request.session['designerID'] = designerID
                context = {
                    'dbuser': dbuser
                }
                if not dbuser[0].PortfolioFilled:
                    return render(request,'designers/portfolioFill.html',context)
                return render(request, 'designers/loggedin.html', context)
            if not dbuser:
                print("Not user")
                return render(request, 'designers/register.html', {})



        else:
            print("not valid")
            return render(request, 'designers/register.html', {})
    else:
       MyRegisterForm=DesignerDetails(request.GET)
       if request.session.has_key('designerID'):
           designerID = request.session['designerID']
           dbuser = Designers.objects.filter(designerID=designerID)
           if dbuser:
               context = {
                   'dbuser': dbuser
               }
               return render(request, 'designers/loggedin.html', context)

       return render(request, 'designers/register.html', {})

class DesignerCreate(CreateView):
    model=Designers
    fields = ['name','firmname','contact','address','profilepic','email','AboutMe','AboutYourDesigns','design1','design2','design3']
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    try:
      del request.session['designerID']
    except:
      pass
    return render(request,'designers/logout.html',{})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):

    if request.session.has_key('designerID'):
        designerID = request.session['designerID']
        dbuser = Designers.objects.filter(designerID=designerID)
        if dbuser:
            user = dbuser[0]
            profilepic = user.profilepic.url
            context={
                'dbuser':dbuser
            }
            return render(request, 'designers/loggedin.html',context)

    return  render(request,'designers/register.html',{})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def regcon(request):
    if request.session.has_key('designerID'):
        designerID = request.session['designerID']
        dbuser = Designers.objects.filter(designerID=designerID)
        if dbuser:
            context = {
                'dbuser': dbuser
            }
            return render(request, 'designers/loggedin.html', context)
    context={

    }
    return render(request,'designers/regconfirm.html',context=context)



def designersview(request):
    all_designers=Designers.objects.exclude(designerID__isnull=True).exclude(designerID__exact='').order_by('-points')
    context = {'all_designers':all_designers}
    return render(request, 'designers/our_designers.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def PortfolioFill(request):
    design2 = None
    design3 = None
    AboutMe = ""
    AboutYourDesigns =""
    if request.method == "POST":
        print("hello")
        PortFolioForm=PortfolioDetails(request.POST)
        print(PortFolioForm.errors)
        if PortFolioForm.is_valid():

            AboutMe = PortFolioForm.cleaned_data['AboutMe']
            print(AboutMe)
            AboutYourDesigns = PortFolioForm.cleaned_data['AboutYourDesigns']
            if request.session.has_key('designerID'):
                designerID = request.session['designerID']
                dbuser = Designers.objects.filter(designerID=designerID)
                user=Designers.objects.get(designerID=designerID)

                user.AboutMe = AboutMe
                user.AboutYourDesigns=AboutYourDesigns
                user.PortfolioFilled=True

                user.save(update_fields=['AboutMe','AboutYourDesigns','PortfolioFilled'])

                context = {
                    'dbuser': dbuser
                }
                return render(request, 'designers/loggedin.html', context)
            else:
                render(request, 'designers/register.html', {})
        else:
            print("invalid form")

    else:
        PortFolioForm=PortfolioDetails(request.GET)
        return render(request, 'designers/portfolioFill.html', {})

    return render(request, 'designers/portfolioFill.html', {})






