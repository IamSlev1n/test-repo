from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list/', BookListView.as_view(), name='book-list'), #list/ added
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('list/<int:pk>', BookDetailView.as_view(), name='book-detail') #list/ added

]

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns += router.urls
