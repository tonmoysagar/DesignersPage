from django import forms
from .models import Designers
class DesignerDetails(forms.Form):
    designerID = forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        print("Hello")
        designerID=self.cleaned_data.get("designerID")
        password=self.cleaned_data("password")
        dbuser=Designers.objects.filter(designerID=designerID)
        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return designerID