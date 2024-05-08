from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class VerifyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_verify=Game.Status.VERIFIED)


# Create your models here.
class Game(models.Model):
    class Status(models.IntegerChoices):
        ON_VERIFICATION = 0, 'На проверке'
        VERIFIED = 1, 'Одобрено'

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    plot = models.TextField(blank=True, verbose_name='Описание')
    release_year = models.DateField(verbose_name='Год выпуска')
    poster = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Обложка', default=None, blank=True, null=True)
    is_verify = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.ON_VERIFICATION, verbose_name='Статус')
    studio = models.ForeignKey('Studio', on_delete=models.PROTECT, related_name='studios', verbose_name='Студия')
    genre = models.ManyToManyField('Genre', blank=True, related_name='genres', verbose_name='Жанр')
    editor = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='games', null=True, default=True )

    # Стандартный manager
    objects = models.Manager()
    # Пользовательский manager
    verify = VerifyManager()

    # Переопределение метода для получения поля имени
    def __str__(self):
        return self.title

    # Определение адреса по slug полю
    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})

    # Переопределение метаданных(используется в админ панеле)
    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'
        ordering = ['id']


class Genre(models.Model):
    title = models.CharField(max_length=120, verbose_name='Жанр')
    slug = models.SlugField(max_length=240, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})

    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'
        ordering = ['id']


class Studio(models.Model):
    title = models.CharField(max_length=120, verbose_name='Студия')
    slug = models.SlugField(max_length=240, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Студии'
        verbose_name_plural = 'Студии'
        ordering = ['id']


class GameUser(models.Model):
    rating = models.FloatField(verbose_name='Оценка', null=False, default=0)
    review = models.TextField(verbose_name='Отзыв', null=False, default="")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user', null=True, default=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game', null=True, default=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        ordering = ['rating']