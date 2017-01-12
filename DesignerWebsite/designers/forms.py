from django import forms
class DesignerDetails(forms.Form):
    designerID = forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput())