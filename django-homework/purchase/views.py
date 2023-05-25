from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = '__all__'
    success_url = '/purchases/'
