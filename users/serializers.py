from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    review_count = serializers.IntegerField(read_only=True)
    recent_reviews = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'password', 'email', 'first_name', 'last_name',
            'created_at', 'updated_at', 'review_count', 'recent_reviews'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_recent_reviews(self, obj):
        reviews = obj.reviews.order_by('-created_at')[:5]
        return [
            {
                "id": r.id,
                "book": {"id": r.book.id, "title": r.book.title},
                "rating": r.rating,
                "created_at": r.created_at
            } for r in reviews
        ]
