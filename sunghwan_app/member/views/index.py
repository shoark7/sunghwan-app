from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse

__all__ = ['index']

# Create your views here.
def index(request):
    return render(request, 'root/base.html')