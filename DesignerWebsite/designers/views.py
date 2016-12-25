from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .  models import Designers
from django import forms
# Create your views here.
def index(request):

    context={

    }
    return render(request,'designers/index.html',context=context)


class DesignerCreate(CreateView):
    model=Designers
    fields = ['name','firmname','contact','address','design','email']
