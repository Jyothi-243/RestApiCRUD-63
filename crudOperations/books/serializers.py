from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = "__all__"  #for some fields ["col1","col2"]