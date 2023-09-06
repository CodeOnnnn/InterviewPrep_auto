from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Response, Question
class Registeruserform(UserCreationForm):
    class Meta:
        model= User
        fields= ['email','username','password1','password2']
        widgets={
            'email':forms.EmailInput(attrs={
                'required':True,
                'placeholder': 'abc@example.com',
                'autofocus': True
            }),
            'username':forms.TextInput(attrs={
                'required':True,
                'placeholder': 'abcxyz1',
            })
        }
    def __init__(self,*args,**kwargs):
        super(Registeruserform,self).__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = {'palceholder':'password'}
        self.fields['password2'].widget.attrs = {'palceholder':'confirm password'}

class LoginForm(AuthenticationForm):
    class Meta:
        fields= '__all__' 

class NewResponseForm(forms.ModelForm):
    class Meta:
        model=Response
        fields=['body']
# class NewReplyForm(forms.ModelForm):
#     class Meta:
#         model = Response
#         fields = ['body']
#         widgets = {
#             'body': forms.Textarea(attrs={
#                 'rows': 2,
#                 'placeholder': 'What are your thoughts?'
#             })
#         }