from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'url', 'title', 'no_of_pages', 'date_published', 'quantity')