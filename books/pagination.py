from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class BookPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_response(self, data):
        return Response({
            'total_books': self.count,  # total number of items
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
