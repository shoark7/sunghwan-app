from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from ..forms import SignupForm
from ..models import CustomUser
import re
from django.contrib import messages
from django.contrib.auth import login as auth_login

__all__ = ['signup',]

def signup(request):
    context = {}
    next = request.GET.get('next')
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            full_name = form.cleaned_data['full_name']
            nickname = form.cleaned_data['nickname']
            phonenumber = form.cleaned_data['phonenumber']
            image = form.cleaned_data['image']

            phonenumber = re.sub(r'(\d{3})-(\d{4})-(\d{4})', r'\1\2\3', phonenumber)

            # 검증 1. 비밀번호
            if password1 != password2:
                context['form'] = form
                messages.error(request, '비밀번호가 다릅니다.')
            else: # 적절함 == 인스턴스를 만듬
                user = CustomUser.objects.create_user(
                    username=username,
                    password=password1,
                    full_name=full_name,
                    nickname=nickname,
                    phonenumber=phonenumber,
                    image=image,
                )
                auth_login(request, user)
                return redirect(next)
        else:
            messages(request, form.errors)
            context['form'] = form

    else:
        context['form'] = SignupForm()
    return render(request, 'member/signup.html', context)

