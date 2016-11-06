from django import forms
from member.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        label='username',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label='password1',
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='password1',
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    full_name = forms.CharField(
        label='full_name',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    nickname = forms.CharField(
        label='nickname',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    phonenumber = forms.CharField(
        label='phonenumber',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    image = forms.ImageField(
        label='image',
        required=False,
    )



