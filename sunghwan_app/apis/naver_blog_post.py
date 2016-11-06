from django.conf import settings
import re
import requests
import json
from bs4 import BeautifulSoup

__all__ =['naver_blog_post']

def naver_blog_post(movie_title, page=1):
    url_front = 'https://openapi.naver.com/v1/search/blog.xml?display=10&start='
    page = int(page)
    page = str(page-1)
    url_back = '1&query='
    full_url = url_front+ page+url_back + '영화 ' + movie_title

    headers = {
        # 'X-Naver-Client-Id': 'eHimOLa8w9EWy7fb4LtZ',
        'X-Naver-Client-Id': settings.CLIENT_ID,
        # 'X-Naver-Client-Secret': 'lfCwzKWnrF',
        'X-Naver-Client-Secret': settings.CLIENT_SECRET,
    }


    blog_text = requests.get(full_url, headers=headers).text
    movie_soup = BeautifulSoup(blog_text, 'xml')

    format = re.compile(r'</?\w+>|&\w+;')
    pre_result = [(format.subn('', item.title.text)[0],
                   format.subn('', item.description.text)[0])
                  for item in movie_soup.find_all('item')]



    return pre_result

naver_blog_post('마미')