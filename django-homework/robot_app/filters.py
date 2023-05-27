import django_filters
from user.models import User
from book.models import Book
from purchase.models import Purchase


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['contains'],
            'last_name': ['contains'],
            'age': ['gt', 'gte', 'lt', 'lte', 'exact']
        }


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'author': ['contains'],
            'year': ['gt', 'gte', 'lt', 'lte', 'exact'],
            'price': ['gt', 'gte', 'lt', 'lte', 'exact']
        }


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user_id': ['exact'],
            'book_id': ['exact']
        }
