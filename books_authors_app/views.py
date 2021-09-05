from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, "books_authors_app/books.html", context)

def addbook(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        title = request.POST["title"]
        desc = request.POST["desc"]
        obj = Book.objects.create(title=title, desc=desc)
        obj.save()
        return redirect('/')

def info_book(request, book_id):
    all_books = Book.objects.all()
    book = Book.objects.get(id=book_id)    
    authors_book = book.authors.all()
    no_authors_books = Author.objects.all().exclude(id__in=authors_book)
    context = {
        'book': book,
        'authors_book': authors_book,
        'no_authors_books': no_authors_books,
    }
    return render(request, "books_authors_app/info_book.html", context)

def add_author_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['authors'])
    author.books.add(book)
    return redirect(f'/books/{book_id}')

def authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, "books_authors_app/authors.html", context)

def addauthor(request):
    if request.method == 'GET':
        return redirect('/authors')
    elif request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        notes = request.POST["notes"]
        obj = Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        obj.save()
        return redirect('/authors')

def info_author(request, author_id):
    all_authors = Author.objects.all()
    author = Author.objects.get(id=author_id)
    books_author = author.books.all()
    no_books_author = Book.objects.all().exclude(id__in = books_author)
    context = {
        'author': author,
        'books_author': books_author,
        'no_books_author': no_books_author,
    }
    return render(request, "books_authors_app/info_author.html", context)

def booktoauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id = request.POST['books'])
    author.books.add(book)
    return redirect(f'/authors/{author_id}')
