from .models import User
from .serializers import UserSerializer
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = '/users/list/'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
