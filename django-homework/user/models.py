from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()

    class Meta:
        db_table = 'user'
