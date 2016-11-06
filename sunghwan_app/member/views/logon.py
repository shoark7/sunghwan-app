from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login,\
    logout as auth_logout

from ..forms import LoginForm

__all__ = ['login', 'logout',]


def login(request):
    next = request.GET.get('next') or ''
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth_authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(next)
            else:
                print('뭔일이지 이게.. ', user)
                context['form'] = LoginForm()

        else:
            context['form'] = form
    else:
        context['form'] = LoginForm()
    return render(request, 'member/login.html', context)


def logout(request):
    next = request.GET.get('next')
    auth_logout(request)

    return redirect(next)