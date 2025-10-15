from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'isbn', 'publication_date', 'average_rating')
    search_fields = ('title', 'isbn')
    list_filter = ('author', 'category', 'publication_date')
