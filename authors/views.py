from rest_framework import generics, status, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ['name']
    filterset_fields = [filters.SearchFilter]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class AuthorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class AuthorDeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        author_id = author.id
        author_name = author.name
        author.delete()
        return Response(
            {"message": f"Author {author_id} ('{author_name}') has been deleted."},
            status=status.HTTP_200_OK
        )
