from mysite.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models

class Book(models.Model):       # 테이블명: app이름_클래스이름 --> books_book
    title   = models.CharField(max_length=100)
    authors  = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name       = models.CharField(max_length=50)
    email      = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name    = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
    
