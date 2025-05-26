from django.db import models

# Create your models here.

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    last_name = models.TextField(max_length=100)
    first_name = models.TextField(max_length=100)
    middle_name = models.TextField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.last_name



class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title

class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_id.first_name
