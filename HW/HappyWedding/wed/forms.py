from django import forms
from wed.models import vendors,enquiry,vendorlisting


class vendorRegForm(forms.ModelForm):
    class Meta:
        model=vendors
        fields=['username','District','phone_number','email','password']

class vendorlistForm(forms.ModelForm):
    class Meta:
        model=vendorlisting
        fields=['Name','vendor','category','company_name','About','District','package','address','image']


class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class enquiryForm(forms.ModelForm):
    class Meta:
        model=enquiry
        fields=['Name','phone_number','district','Event_date','Event_detail','vendor']
        














    



        


    
