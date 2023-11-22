from django.db.models import Q
from django.views.generic import ListView
from .models import Book


class BookList(ListView):
    model = Book
    template_name = 'library_app/index.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Все книги'
        return context


class GenreDetail(ListView):
    template_name = 'library_app/index.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.filter(genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Книги в жанре: ' + str(self.get_queryset()[0].genre)
        return context


class SearchResult(ListView):
    template_name = 'library_app/search_result.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = ''
        if query:
            results = Book.objects.filter(Q(book_title__icontains=query))
        return results

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Результаты поиска'
        return context

