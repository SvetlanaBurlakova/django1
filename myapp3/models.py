from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age:{self.age}'

class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthdate = models.DateField(default=timezone.now())

    @property
    def fullname(self):
        return f'{self.name} {self.lastname}'


    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'Title is {self.title}'
