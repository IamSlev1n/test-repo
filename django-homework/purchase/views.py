from .models import Purchase
from .serializers import PurchaseSerializer
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = '__all__'
    success_url = '/purchases/list/'


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

