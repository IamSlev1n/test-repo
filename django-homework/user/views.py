import django_filters
from .models import User
from .serializers import UserSerializer
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from robot_app.filters import UserFilter


# Create your views here.
class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = '/users/list/'


class UserViewSetPagination(PageNumberPagination):
    page_size = 10


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    pagination_class = UserViewSetPagination
    search_fields = ['first_name', 'last_name', ]
    ordering_fields = ['age', 'id', ]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

