from django.urls import path
from .views import UserListCreateView, UserDetailUpdateView, UserDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailUpdateView.as_view(), name='user-detail-update'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),
]
