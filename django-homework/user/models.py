from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

    def is_adult(self):
        return True if self.age >= 18 else False