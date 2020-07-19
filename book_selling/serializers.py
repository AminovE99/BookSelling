# -*- coding:utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from book_selling.models import Book, Author


class AuthorSerializer(ModelSerializer):
    books = serializers.SerializerMethodField('get_books')

    class Meta:
        model = Author
        fields = ('fio', 'books')


class RawAuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'middle_name')


class BookSerializer(ModelSerializer):
    authors = RawAuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'price')
