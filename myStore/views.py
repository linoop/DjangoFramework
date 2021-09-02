from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Book, Game
from .serializers import BookSerializers


@api_view(['GET'])
def allBooks(request):
    articles = Book.objects.all()
    serializer = BookSerializers(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, key):
    article = Book.objects.get(id=key)
    serializer = BookSerializers(article, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def insertBook(request):
    serializer = BookSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateBook(request, key):
    article = Book.objects.get(id=key)
    serializer = BookSerializers(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBook(request, key):
    article = Book.objects.get(id=key)
    article.delete()
    return Response('Book deleted successfully')


def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New products')


def home_page(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

