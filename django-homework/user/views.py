from .models import User
from .forms import UserForm
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = '/users/'
