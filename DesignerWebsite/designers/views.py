from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .  models import Designers
from . forms import DesignerDetails
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
        else:
            print("not valid")
    else:
       MyRegisterForm=DesignerDetails(request.GET)
    return render(request,'designers/register.html',{'designerID':designerID,'password':password})

class DesignerCreate(CreateView):
    model=Designers
    fields = ['name','firmname','contact','address','design','email']
