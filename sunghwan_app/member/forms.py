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
        label='ID',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    full_name = forms.CharField(
        label='이름',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    nickname = forms.CharField(
        label='별명',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    phonenumber = forms.CharField(
        label='휴대폰 번호',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    image = forms.ImageField(
        label='회원 사진',
        required=False,
    )



