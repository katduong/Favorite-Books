from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from apps.application.models import User
from .models import Book
from django.contrib import messages

# Create your views here.
def index(request):
    if 'userid' not in request.session:
        return redirect(reverse('home:index'))
    else:
        user = User.objects.get(id=request.session['userid'])
        books = Book.objects.all()
        context = {
            "user": user,
            "allBooks": books,
        }
    return render(request, "books/index.html", context)

def add(request):
    errors = Book.objects.bookValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect("/books")
    else:
        title = request.POST['title']
        description = request.POST['description']
        uploader = User.objects.get(id=request.session['userid'])
        newBook = Book.objects.create(title=title, description=description, uploader=uploader)
        newBook.usersWhoLike.add(uploader)
        return redirect("/books")

def showBook(request, bookId):
    book = Book.objects.get(id=bookId)
    uploader = book.uploader
    user = User.objects.get(id=request.session['userid'])
    context = {
        'book': Book.objects.get(id=bookId),
        'user': User.objects.get(id=request.session['userid'])
    }
    if request.session['userid'] == uploader.id:
        return render(request, "books/editBook.html", context)
    else:
        return render(request, "books/showBook.html", context)

def addFavorite(request, bookId):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=bookId)
    book.usersWhoLike.add(user)
    return redirect("/books/" + bookId)

def unFavorite(request, bookId):
    user = User.objects.get(id=request.session['userid'])
    print(bookId)
    book = Book.objects.get(id=bookId)
    book.usersWhoLike.remove(user)
    return redirect("/books/" + bookId)

def deleteBook(request, bookId):
    book = Book.objects.get(id=bookId)
    book.delete()
    return redirect("/books")

def updateBook(request, bookId):
    book = Book.objects.get(id=bookId)
    book.title = request.POST['title']
    book.description = request.POST['description']
    book.save()
    return redirect("/books/" + bookId)

def addFavoriteHome(request, bookId):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=bookId)
    book.usersWhoLike.add(user)
    return redirect("/books")
