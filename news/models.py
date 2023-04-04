from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class News(models.Model):   
    
    name = models.CharField(max_length=100, unique=True, )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to = 'Category',
        on_delete = models.CASCADE,
        related_name = 'news'
    )

    def __str__(self):
        return f"{self.name.title()}: {self.description[:20]}"
        
    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
