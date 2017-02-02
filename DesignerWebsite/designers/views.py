from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .  models import Designers
from . forms import DesignerDetails,PortfolioDetails,ConfirmPasswordForm
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
        form_errors= MyRegisterForm.errors
        content={
            'form':MyRegisterForm,
            'errors':  form_errors
        }
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
    fields = ['name','firmname','contact','address','email']


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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def designersview(request):
    all_designers=Designers.objects.exclude(designerID__isnull=True).exclude(designerID__exact='').order_by('-points')
    context = {'all_designers':all_designers}
    return render(request, 'designers/our_designers.html',context)


def PortfolioFill(request):
    if not request.session.has_key('designerID'):
        return render(request, 'designers/register.html', {})
    design2 = None
    design3 = None
    AboutMe = ""
    AboutYourDesigns =""
    if request.method == "POST":

        PortFolioForm=PortfolioDetails(request.POST)
        print(PortFolioForm.errors)
        if PortFolioForm.is_valid():

            AboutMe = PortFolioForm.cleaned_data['AboutMe']
            print(AboutMe)
            AboutYourDesigns = PortFolioForm.cleaned_data['AboutYourDesigns']
            design2=request.FILES['design2']
            design3 = request.FILES['design3']
            if request.session.has_key('designerID'):
                designerID = request.session['designerID']
                dbuser = Designers.objects.filter(designerID=designerID)
                user=Designers.objects.get(designerID=designerID)
                user.AboutMe = AboutMe
                user.AboutYourDesigns=AboutYourDesigns
                user.PortfolioFilled=True
                user.design2=design2
                user.design3=design3

                user.save(update_fields=['AboutMe','AboutYourDesigns','PortfolioFilled','design2','design3'])

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

    return render(request, 'designers/register.html.html', {})


def change_password(request):
    if not request.session.has_key('designerID'):
        return render(request, 'designers/register.html', {})
    old_password=""
    new_password=""
    if request.session.has_key('designerID') and request.method == "POST":
        MyForm=ConfirmPasswordForm(request.POST)
        print(MyForm.errors)
        if MyForm.is_valid():
            old_password=MyForm.cleaned_data['old_password']
            new_password = MyForm.cleaned_data['new_password']
            print(old_password)
            if request.session.has_key('designerID'):
                designerID = request.session['designerID']
                user = Designers.objects.get(designerID=designerID)
                if user and user.password==old_password:
                    dbuser = Designers.objects.filter(designerID=designerID,password=old_password)
                    user.password = new_password
                    user.save(update_fields=['password'])
                    dbuser = Designers.objects.filter(designerID=designerID)
                    if dbuser:
                        user = dbuser[0]
                        profilepic = user.profilepic.url

                        context = {
                            'dbuser': dbuser
                        }
                        return render(request, 'designers/loggedin.html', context)
                else:
                    print('not user ')
                    del request.session['designerID']
                    return render(request, 'designers/WrongPassword.html', {})
    elif request.session.has_key('designerID') and request.method=="GET":
        return render(request,'designers/changePassword.html',{})


    return render(request,'designers/index.html',{})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def wrongPassword(request):
    if not request.session.has_key('designerID'):
        return render(request, 'designers/register.html', {})
    return render(request, 'designers/WrongPassword.html', {})





