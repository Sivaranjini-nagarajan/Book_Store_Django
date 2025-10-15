from rest_framework import serializers
from .models import Book
from reviews.models import Review
from categories.models import Category
from authors.models import Author

class AuthorSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

class CategorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class BookSerializer(serializers.ModelSerializer):
    author=AuthorSummarySerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True, source='author'
    )
    category=CategorySummarySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'isbn', 'publication_date',
            'author', 'author_id', 'category', 'category_id', 'average_rating', 'review_count'
        ]

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(book=obj)
        if reviews.exists():
            return round(reviews.aggregate(avg=serializers.models.Avg('rating'))['avg'], 2)
        return 0.0

    def get_review_count(self, obj):
        return Review.objects.filter(book=obj).count()