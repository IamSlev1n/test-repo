from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>', UserDetailView.as_view(), name='user-detail')

]
