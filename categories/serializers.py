from rest_framework import serializers
from .models import Category
from books.serializers import BookSerializer

class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'books', 'created_at', 'updated_at']
