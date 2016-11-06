from django.shortcuts import render, redirect, get_object_or_404
from ..models import Movie
from django.contrib import messages

__all__ = ['movie_detail',]


def movie_detail(request, movie_id):
    try:
        movie = get_object_or_404(Movie, id=movie_id)
    except:
        messages.error(request, '그런 영화 또 없습니다.')
        return redirect('sunghwan:movie_list')

    context = {
        'movie': movie,
    }
    return render(request, 'sunghwan_park/movie_detail.html', context)