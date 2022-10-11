from django.contrib import admin

from mylibrary.models import Book, Person, Lend

# Register your models here.
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Lend)

