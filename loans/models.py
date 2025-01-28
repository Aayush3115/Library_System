from django.db import models
from users.models import User
from books.models import Book  # Adjust the import path as necessary
# Create your models here.

class Loan(models.Model):

    def get_uerr_model():
        from django.contrib.auth import get_user
        return get_user_model()
    


    user=models.ForeignKey(User, on_delete=models.CASCADE)  
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'