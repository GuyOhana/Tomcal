from ast import And
import pkgutil
from ssl import AlertDescription
import string
from urllib import request
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.template import loader
from mylibrary.models import Book, Lend, Person
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    books = Book.objects.all()
    persons = Person.objects.all()
    lends = Lend.objects.all()
    return render(request,"index.html",{"Books": books, "Persons": persons,"Lends": lends})

# Create your views here.

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("index")

def delete_person(request, person_id):
    person = Person.objects.get(person_id= person_id)
    lend = Lend.objects.all()
    for item in lend:
        if(item.person.person_id == person_id and item.is_currently_lending):
            book = Book.objects.get(pk = item.book.id)
            book.count_lending = book.count_lending -1
            book.save()
    person.delete()
    return redirect("index")

def add_person(request):
    if request.method == "POST":
        # Take in the data the user submitted and save it 
        person_id = request.POST['person_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        person = Person( person_id = person_id, first_name = first_name, last_name = last_name)
        person.save()
        return redirect("index")
    return render(request,"add_person.html")

def update_person(request,person_id):
    person = Person.objects.get(pk = person_id)
    template = loader.get_template('update_person.html')
    context = {
    'person': person,
    }
    return HttpResponse(template.render(context, request))
  
def updaterecord(request, person_id):
    person = Person.objects.get(pk=person_id)
    person_id = request.POST['person_id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    person.delete()
    person.first_name = first_name
    person.last_name = last_name
    person.person_id = person_id
    person.save()
    return redirect("index")

def stop_lending_to_person(request, lend_id):
    lend = Lend.objects.get(id= lend_id)
    lend.is_currently_lending = False
    lend.save()
    # updates the lending count
    book = Book.objects.get(id= lend.book.id)
    book.count_lending =book.count_lending - 1
    book.save()
    return redirect("index")

def lend_book_choose_person(request, book_id):
    book = Book.objects.get(pk=book_id)
    persons = Person.objects.all()
    if request.method == "POST":
        # Take in the data the user submitted and save it 
        person_id = request.POST['person_id']
        person = Person.objects.get(pk=person_id)
        book.count_lending = book.count_lending+1
        book.save()
        lend = Lend( book = book, person = person, is_currently_lending = True)
        lend.save()
        return redirect("index")
    return render(request,"lend_book_choose_person.html",{"Persons": persons,"book_id": book_id})

