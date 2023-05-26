from .models import Purchase
from .serializers import PurchaseSerializer
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
import django_filters


# Create your views here.
class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = '__all__'
    success_url = '/purchases/list/'


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user_id': ['exact'],
            'book_id': ['exact']
        }


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    search_fields = ['book_id', 'user_id', ]
    ordering_fields = ['book_id', 'user_id', ]
    filter_backends = {
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    }

