from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    """Пост"""
    title = models.CharField('Название',max_length=100)
    description = models.TextField("Описание")
    date = models.DateTimeField("Дата публикации",default=datetime.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Пост'
        verbose_name_plural = 'Посты'
