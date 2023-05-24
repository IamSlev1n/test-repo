from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    path('create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail')

]