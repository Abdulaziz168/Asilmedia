from django.contrib.auth.forms import UserCreationForm
from django import forms  

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150,widget=forms.TextInput(attrs={'class': 'username','id':'username'}))  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'password','id':'password'}))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
