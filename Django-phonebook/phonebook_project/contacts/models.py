# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import User

class Phonebook(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    phonebooks = models.ManyToManyField(Phonebook, related_name='contacts')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CallRecords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)        # whom the callrecords belongs to  (the main user who is logged in)
    username = models.CharField(max_length=20)          # whom we are calling to
    call_timestamp = models.DateTimeField()
    duration = models.CharField(max_length=50)
    phonenum = models.CharField(max_length=20)
    call_cost = models.CharField(max_length=20)
    call_result= models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}"
