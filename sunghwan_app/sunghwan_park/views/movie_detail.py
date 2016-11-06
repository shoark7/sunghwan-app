from django.shortcuts import render, redirect, get_object_or_404
from ..models import Movie
from django.contrib import messages
from apis import naver_blog_post
from django.contrib.auth.decorators import login_required

__all__ = ['movie_detail',]


@login_required
def movie_detail(request, movie_id):
    page = request.GET.get('page') or '1'

    try:
        movie = get_object_or_404(Movie, id=movie_id)
    except:
        messages.error(request, '그런 영화 또 없습니다.')
        return redirect('sunghwan:movie_list')

    else:
        blog_post_list = naver_blog_post(movie.title, page)
        context = {
            'movie': movie,
            'blog_post_list': blog_post_list
        }

    return render(request, 'sunghwan_park/movie_detail.html', context)