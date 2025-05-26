from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __repr__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    
    
