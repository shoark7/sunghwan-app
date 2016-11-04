from django.db import models

# Create your models here.
class Movie(models.Model):
    # 제목, 감독, 장르, 한줄평, 개인 평점, 관람 날짜
    title = models.CharField(max_length=20, unique=True)
    director = models.CharField(max_length=20)
    genre = models.CharField(max_length=10)
    my_comment = models.TextField(default='')
    my_score = models.FloatField(default=0.0)
    watched_date = models.DateField()
    img_thumbnail = models.ImageField(upload_to='movie', blank=True, null=True)


    def __str__(self):
        return self.title

"""
    def save(self, kwargs={'force_insert':False}):
        import os
        from PIL import Image, ImageOps
        from io import BytesIO
        from django.core.files.base import ContentFile
        import requests
        from django.core.files.storage import default_storage

        img_source = requests.get(self.img_thumbnail).content
        img_bytes = BytesIO(img_source)
        image = Image.open(img_bytes)

        ftype = image.format

        # 기존에 있던 img의 경로와 확장자를 가져옴
        path, ext = os.path.splitext(self.img_thumbnail.name)
        name = os.path.basename(path)
        name = self.title+ext

        thumbnail_name = '%s_thumb%s' % (name, ext)
        # 기존파일명_thumb.확장자 형태가 됨

        ###################################################

        # 임시 파일로 취급되는 객체 생성
        temp_file = BytesIO()
        image.save(temp_file, ftype)
        temp_file.seek(0)

        # img_thumbnail필드에 해당 파일내용을 저장
        # Django의 FileField에 내용을 저장할때는 ContentFile형식이어야 함
        content_file = ContentFile(temp_file.read())
        # print('type of img_thumbnail is {}'.format(type(self.img_thumbnail)))
        self.img_thumbnail.save(name, content_file)

        # 열었던 파일 닫아줌
        temp_file.close()
        content_file.close()

        return True
"""

