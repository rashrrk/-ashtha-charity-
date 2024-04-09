from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from .models import UserProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password')
        
    def __init__(self, *args, **kwargs):
        super( CreateUserForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['email'].widgets.attrs['class']='form-control'
        self.fields['phone number'].widgets.attrs['class']='form-control'
        self.fields['password'].widgets.attrs['class']='form-control'