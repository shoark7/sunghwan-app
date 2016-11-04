from django.shortcuts import render, redirect, get_object_or_404
from openpyxl import load_workbook
from django.conf import settings
from django.http import HttpResponse
from bs4 import BeautifulSoup
from sunghwan_park.models import Movie
import os
import requests
from django.contrib import messages

# Create your views here.
__all__ = ['movie_list', 'movie_update',]

def movie_list(request):
    pass


def movie_update(request):
    """
    This function is only for administrators.
    Compare the excel file to the exsiting Movie model.
    If new movie is written, make a new Movie model instance with a photo given by bs4
    :param request:
    :return: none. Just Movie model update
    """

    # Check if a new movie is added
    movies = Movie.objects.all()
    movie_titles = [movie.title for movie in movies]

    xl_directory_name = os.path.join(settings.STATIC_DIR, 'others/박성환 영화 희망 및 관람 목록.xlsx')
    wb = load_workbook(xl_directory_name)

    # need refactoring. We have 3 sheets but only 1 sheet is provided

    # 0 : watch_or_not, 1: title, 2: director, 3: genre,
    # 4: my_comment , 5: my_score, 6: watched_date,
    ws = wb.worksheets[1]
    new_movies = []
    for row in ws.rows:
        if row[0].value != 'a': # 'a' means 'watched or not'
            continue
        elif row[1].value not in movie_titles:
            new_movies.append(row)

    if not new_movies:
        messages.info(request, "새 영화가 없습니다.")
        return HttpResponse("새 영화가 없습니다.")

    else: # if new movies exist
        naver_movie_search_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='

        for row in new_movies:
            full_url = naver_movie_search_url+row[1].value.replace(' ', '')
            movie_text = requests.get(full_url)
            soup = BeautifulSoup(movie_text, 'html.parser')