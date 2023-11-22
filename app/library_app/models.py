from django.db import models


class Book(models.Model):
    book_title = models.CharField(max_length=250, verbose_name='Название')
    author = models.CharField(max_length=250, verbose_name='Автор')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='books', verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['book_title']

    def __str__(self):
        return self.book_title


class Genre(models.Model):
    genre_title = models.CharField(max_length=250, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['genre_title']

    def __str__(self):
        return self.genre_title
