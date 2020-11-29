from rest_framework.serializers import ModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import * 

class DistrictSerializer(ModelSerializer):
    class Meta: 
        model = District
        fields = "__all__"

class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"

class LibrarySerializer(WritableNestedModelSerializer):
    district = DistrictSerializer()
    class Meta:
        model = Library
        fields = "__all__"
    
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(WritableNestedModelSerializer):
    library = LibrarySerializer(many=True)
    author_name = AuthorSerializer()
    category = CategorySerializer()
    class Meta: 
        model = Book
        fields = "__all__"

class BookLibrarySerializer(ModelSerializer):
    library = LibrarySerializer(many=True)
    class Meta: 
        model = Book
        fields = ("id","library")