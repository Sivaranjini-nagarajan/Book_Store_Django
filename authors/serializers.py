from rest_framework import serializers
from .models import Author
from books.models import Book

class BookSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'publication_date']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSummarySerializer(many=True, read_only=True)
    book_count = serializers.IntegerField(source='books.count', read_only=True)

    class Meta:
        model = Author
        fields = [
            'id', 'name', 'biography', 'birth_date', 'death_date',
            'country', 'book_count', 'books', 'created_at', 'updated_at'
        ]
