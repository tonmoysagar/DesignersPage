from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .  models import Designers
from . forms import DesignerDetails
from django.http import Http404
# Create your views here.
def index(request):

    context={

    }
    return render(request,'designers/index.html',context=context)

def registeration(request):
    designerID=""

    password=""
    if request.method == "POST":
        # Get the posted form
        MyRegisterForm = DesignerDetails(request.POST)
        content={'form':MyRegisterForm}
        print( MyRegisterForm.errors)
        if MyRegisterForm.is_valid():
            designerID=MyRegisterForm.cleaned_data['designerID']

            password=MyRegisterForm.cleaned_data['password']
            print(designerID)
            dbuser = Designers.objects.filter(designerID=designerID,password=password)
            if not dbuser:
                print("Not user")
                return render(request, 'designers/register.html', {})


            else:
                print(dbuser)
                return render(request,'designers/loggedin.html',{'designerID':designerID})

        else:
            print("not valid")
            return render(request, 'designers/register.html', {})
    else:
       MyRegisterForm=DesignerDetails(request.GET)
       return render(request, 'designers/register.html', {})

class DesignerCreate(CreateView):
    model=Designers
    fields = ['name','firmname','contact','address','design','email']
