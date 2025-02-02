from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    copies_available = models.PositiveBigIntegerField(default=0, null=False, blank=False)
    description = models.TextField(null=True, blank=True)   

    def __str__(self):
        return self.title