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
