from django.shortcuts import render, redirect, get_object_or_404
from openpyxl import load_workbook
from django.http import HttpResponse
from bs4 import BeautifulSoup
from sunghwan_park.models import Movie
from django.conf import settings
import os
import requests
from django.contrib import messages
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from sunghwan_app.custom_storages import StaticStorage
from sunghwan_park import tasks


# Create your views here.
__all__ = ['movie_list', 'movie_update',]


@login_required
def movie_list(request):
    if request.method == 'POST':
        order_criteria = request.POST['order-criteria']
        movies = Movie.objects.order_by('-'+order_criteria)
    else:
        movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'sunghwan_park/movie_list.html', context)


@staff_member_required
def movie_update(request):
    """
    This function is only for administrators.
    Compare the excel file to the existing Movie model instances.
    If any new movies are written, make new Movie model instances with a photo given by bs4.
    :param request:
    :return: none. Just Movie model update for the administrator.
    """
    # static_storage = StaticStorage()
    # wb = load_workbook(static_storage.open('others/박성환 영화 희망 및 관람 목록.xlsx'))

    # Check if a new movie is added

    tasks.movie_list_update(request)
    return redirect('member:index')


# 0 : watch_or_not, 1: title, 2: director, 3: genre,
# 4: my_comment , 5: my_score, 6: watched_date,
