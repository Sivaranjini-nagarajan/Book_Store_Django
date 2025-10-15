from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer
from books.models import Book
from django.shortcuts import get_object_or_404

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  # no auth for creating
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        if book_id is not None:
            queryset = Review.objects.filter(book_id=book_id)
        else:
            queryset = Review.objects.none()

        rating = self.request.query_params.get('rating')
        order_by = self.request.query_params.get('order_by', 'newest')

        if rating:
            queryset = queryset.filter(rating=rating)

        if order_by == 'highest_rated':
            queryset = queryset.order_by('-rating', '-created_at')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset

    def perform_create(self, serializer):
        book_id = self.kwargs['book_id']
        book = get_object_or_404(Book, id=book_id)
        serializer.save(user=self.request.user, book=book)


class ReviewDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        if book_id is not None:
            return Review.objects.filter(book_id=book_id)
        return Review.objects.none()

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("You can only update your own reviews.")
        serializer.save()

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        review_id = review.id
        review.delete()
        return Response(
            {"message": f"Review {review_id} has been deleted."},
            status=status.HTTP_200_OK
        )