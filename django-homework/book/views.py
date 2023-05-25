from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer


# Create your views here.
class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/list/'


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
