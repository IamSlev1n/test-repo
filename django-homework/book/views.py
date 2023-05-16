from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from book.models import Book
import json


# Create your views here.
def books_view(request):
    books = Book.objects.all().values()
    data = {"books": list(books)}
    return JsonResponse(data)
