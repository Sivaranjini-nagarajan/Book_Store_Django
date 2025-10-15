from django.urls import path
from .views import AuthorListCreateView, AuthorRetrieveUpdateView, AuthorDeleteView

urlpatterns = [
    path('', AuthorListCreateView.as_view(), name='author-list-create'),
    path('<int:pk>/', AuthorRetrieveUpdateView.as_view(), name='author-detail-update'),
    path('<int:pk>/delete', AuthorDeleteView.as_view(), name='author-delete'),
]
