from rest_framework import serializers
from . models import Book, Game


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class GamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

