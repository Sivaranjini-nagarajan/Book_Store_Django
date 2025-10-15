from rest_framework import serializers
from .models import Review
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)
    book_id = serializers.IntegerField(source='book.id', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'book_id', 'user', 'rating', 'title', 'content', 'created_at', 'updated_at']
