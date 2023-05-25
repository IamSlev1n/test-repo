from .models import Book
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
