from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Designers(models.Model):
    designerID=models.CharField(max_length=15)
    password=models.CharField(max_length=8,null=True)



    def get_absolute_url(self):
        return reverse('index')


    def __str__(self):
        return self.name+' '+ self.firmname+' '+self.address

class Designer(models.Model):
    designerPro=models.ForeignKey(Designers,on_delete=models.CASCADE)
