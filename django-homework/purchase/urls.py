from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list/', PurchaseListView.as_view(), name='purchase-list'), #list/ added
    path('create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('list/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail') #list/ added

]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
