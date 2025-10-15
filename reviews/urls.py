from django.urls import path
from .views import ReviewListCreateView, ReviewDetailUpdateView, ReviewDeleteView

app_name = "reviews"
urlpatterns = [
    path('books/<int:book_id>/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('books/<int:book_id>/<int:pk>/', ReviewDetailUpdateView.as_view(), name='review-detail-update'),
    path('books/<int:book_id>/<int:pk>/delete', ReviewDeleteView.as_view(), name='review-delete'),
]
