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


def movie_update(request):
    """
    This function is only for administrators.
    Compare the excel file to the existing Movie model instances.
    If any new movies are written, make new Movie model instances with a photo given by bs4.
    :param request:
    :return: none. Just Movie model update for the administrator.
    """

    # Check if a new movie is added
    movies = Movie.objects.all()
    movie_titles = [movie.title for movie in movies]

    xl_directory_name = os.path.join(settings.STATIC_DIR, 'others/박성환 영화 희망 및 관람 목록.xlsx')
    wb = load_workbook(xl_directory_name)

    # 0 : watch_or_not, 1: title, 2: director, 3: genre,
    # 4: my_comment , 5: my_score, 6: watched_date,

    new_movies = []
    worksheets = wb.worksheets

    for ws in worksheets:
        for row in ws.rows:
            if row[0].value != 'a': # 'a' means 'watched or not'
                continue
            elif row[1].value not in movie_titles:
                new_movies.append(row)

    if not new_movies:
        messages.info(request, "새 영화가 없습니다.")
        return HttpResponse("새 영화가 없습니다.")

    else: # if new movies exist
        headers = {
                    'X-Naver-Client-Id': settings.CLIENT_ID,
                    'X-Naver-Client-Secret': settings.CLIENT_SECRET,
                  }
        url = 'https://openapi.naver.com/v1/search/movie.xml?display=1&query='


        for row in new_movies:
            full_url = url+row[1].value.replace(' ', '')
            movie_text = requests.get(full_url, headers=headers).text
            soup = BeautifulSoup(movie_text, 'xml')
            try:
                img_url = soup.channel.item.image.string
            except:
                img_url = None

            movie = Movie(
                title=row[1].value,
                director=row[2].value,
                genre=row[3].value,
                my_comment=row[4].value,
                my_score=float(row[5].value),
                watched_date=row[6].value,
            )

            if not img_url:
                movie.save()

            else:
                img_source = requests.get(img_url).content
                bytes_file = BytesIO(img_source)
                image = Image.open(bytes_file)
                image_format = image.format
                temp_file = BytesIO()
                image.save(temp_file, image_format)
                temp_file.seek(0)

                path, ext = os.path.splitext(img_url)
                name = os.path.basename(path)
                # print(name, ext)
                img_name = '%s%s' % (name, ext)

                movie.img_thumbnail.save(img_name, ContentFile(temp_file.read()))
                movie.save()
                # print(movie)

            # movie = Movie.objects.create(
            #     title=row[1].value,
            #     director=row[2].value,
            #     genre=row[3].value,
            #     my_comment=row[4].value,
            #     my_score=float(row[5].value),
            #     watched_date=row[6].value,
            #     img_thumbnail=img_url
            # )
        # Time for making it csvs
        # movies = Movie.objects.all()

        return redirect('member:index')

# 0 : watch_or_not, 1: title, 2: director, 3: genre,
# 4: my_comment , 5: my_score, 6: watched_date,
