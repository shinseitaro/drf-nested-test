from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import * 
from .serializers import * 

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

class LibraryViewSet(ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

# nested routers view
class BookLibraryViewSet(ReadOnlyModelViewSet):
    serializer_class = BookLibrarySerializer
    def get_queryset(self):
        book_pk = self.kwargs.get("book_pk")
        return Book.objects.filter(pk=book_pk)

class AuthorBookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_pk = self.kwargs.get("author_pk")
        # FK で繋がっているデータは select_related でマージ
        # マージした時に author_pk をauthor_nameとしてマージされる
        queryset = Book.objects.all().select_related("author_name") 
        return queryset.filter(author_name=author_pk)

class LibraryBookViewSet(ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        library_pk = self.kwargs.get("library_pk")
        queryset = Book.objects.all().prefetch_related("library")
        return queryset.filter(library=library_pk)