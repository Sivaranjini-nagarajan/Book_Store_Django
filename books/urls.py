from django.urls import path
from .views import BookListCreateView, BookDetailUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookDetailUpdateView.as_view(), name='book-detail-update'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
]
