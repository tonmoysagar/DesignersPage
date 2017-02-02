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


class PortfolioDetails(forms.Form):
    AboutMe=forms.CharField(max_length=200)
    AboutYourDesigns=forms.CharField(max_length=300)

    def clean_message(self):

        cleaned_data=super(PortfolioDetails, self).clean()
        AboutMe=cleaned_data.get("AboutMe")
        AboutYourDesigns=cleaned_data.get("AboutYourDesigns")
        return AboutMe