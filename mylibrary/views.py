import pkgutil
import string
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.template import loader
from mylibrary.models import Book, Person
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    books = Book.objects.all()
    persons = Person.objects.all()
    return render(request,"index.html",{"Books": books, "Persons": persons})

# Create your views here.

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("index")

def delete_person(request, person_id):
    person = Person.objects.get(person_id= person_id)
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



