from django.shortcuts import render,get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating") #order_by() can also be included here, add - sign in front of field for desc order
    total = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html",{
        "books": books,
        "total_books":total,
        "avg_rating": avg_rating

    })


def book_detail(request,slug):
    # try:
    #     book = Book.objects.get(id=id)  # pk=id is also valid as id is set as primary key in db
    # except:
    #     raise Http404()
    book = get_object_or_404(Book,slug=slug)
    return render(request, "book_outlet/book_details.html",{
        "title" : book.title,
        "author": book.author,
        "rating": book.rating,
        "bestselling": book.is_bestselling

    })