from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserChangeForm
from .models import User


class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self)
        print(f"password={self.cleaned_data.get('password')}")
        # user.set_password(self.cleaned_data.get('password'))        

        if commit:
            user.save()
            
        return user




class LoginForm(Form):
    class Meta(Form):
        model = User
        fields = ['email', 'password']

