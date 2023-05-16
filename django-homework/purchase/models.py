from django.db import models
from user.models import User
from book.models import Book


# Create your models here.
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        db_table = 'purchase'
        ordering = ['-date']

