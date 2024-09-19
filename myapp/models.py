from django.db import models

class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 

    def __str__(self):
        return self.username

# models.py
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(max_length=100)
    description = models.TextField(max_length=100)

#test