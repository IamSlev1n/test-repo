from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'book'
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book')
        ]

    def __str__(self):
        return f"{self.title}: {self.author} ; year: {self.year}"
