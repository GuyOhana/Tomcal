from email.policy import default
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    num_copies = models.IntegerField()
    image_url = models.CharField(max_length=80000)
    count_lending = models.IntegerField(default = 0)
    def __str__(self):
        return self.title

class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name +" "+self.last_name


class Lend(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    is_currently_lending = models.BooleanField( default = True)

