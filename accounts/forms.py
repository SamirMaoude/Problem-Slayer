from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class ProblemSlayerUserForm(UserCreationForm):



    

    class Meta:
        model = User

        fields = ['first_name','last_name','email','username','password1','password2']

        widgets = {
            'first_name' : forms.TextInput(),
            'last_name' :  forms.TextInput(),
            'email' : forms.EmailInput(),
            'username' : forms.TextInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput()
        }