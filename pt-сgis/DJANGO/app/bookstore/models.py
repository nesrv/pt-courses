from django.db import models


class Book(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.author}, {self.title}'

    
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'