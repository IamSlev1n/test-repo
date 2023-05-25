from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView, UserViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'), #list/ added
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('list/<int:pk>', UserDetailView.as_view(), name='user-detail') #list/ added

]

router = SimpleRouter()
router.register('', UserViewSet)


urlpatterns += router.urls
