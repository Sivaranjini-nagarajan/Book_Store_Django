from django.urls import path
from .views import CategoryListCreateView, CategoryDetailUpdateView, CategoryDeleteView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetailUpdateView.as_view(), name='category-detail-update'),
    path('<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
]
