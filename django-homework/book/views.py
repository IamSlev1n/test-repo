from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
import django_filters
from rest_framework import filters


# Create your views here.
class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/list/'


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'author': ['contains'],
            'year': ['gt', 'gte', 'lt', 'lte', 'exact'],
            'price': ['gt', 'gte', 'lt', 'lte', 'exact']
        }


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ['title', 'author', ]
    ordering_fields = ['price', 'year', ]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
