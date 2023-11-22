from django.contrib import admin
from .models import Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'author', 'genre']
    prepopulated_fields = {'slug': ('book_title',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_title', 'slug']
    prepopulated_fields = {'slug': ('genre_title',)}
