from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Designers(models.Model):
    designerID=models.CharField(max_length=15)
    name=models.CharField(max_length=25,null=True)
    firmname=models.CharField(max_length=30,null=True)
    contact=models.CharField(max_length=10,null=True)
    address=models.TextField(max_length=200,null=True)
    profilepic=models.ImageField(null=True)
    email=models.EmailField(max_length=30,null=True)
    password=models.CharField(max_length=10,null=True)
    points=models.IntegerField(null=True,default=100)
    design1=models.ImageField(null=True)
    design2=models.ImageField(null=True,blank=True)
    design3=models.ImageField(null=True,blank=True)
    AboutMe=models.TextField(max_length=200,null=True,default="Please tell us about your personallity and why shoud customers be interested in you")
    AboutYourDesigns=models.TextField(max_length=200,null=True,default="Please tell us about your design styles")
    PortfolioFilled=models.BooleanField(default=False)



    def get_absolute_url(self):
        return reverse('designers:regcon')


    def __str__(self):
        return self.name+' '+ self.firmname+' '+self.address+' '+self.AboutMe

class Designer(models.Model):
    designerPro=models.ForeignKey(Designers,on_delete=models.CASCADE)
