from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Designers(models.Model):
    designerID=models.CharField(max_length=15)
    name=models.CharField(max_length=250)
    firmname=models.CharField(max_length=300)
    contact=models.CharField(max_length=13)
    address=models.CharField(max_length=500)
    design=models.FileField(null=True)
    points=models.IntegerField(default=100)
    email=models.CharField(max_length=150,null=True)


    def get_absolute_url(self):
        return reverse('index')


    def __str__(self):
        return self.name+' '+ self.firmname+' '+self.address

class Designer(models.Model):
    designerPro=models.ForeignKey(Designers,on_delete=models.CASCADE)
