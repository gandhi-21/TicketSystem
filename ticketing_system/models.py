from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    username = models.CharField(max_length=20, unique=True, default="username")
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    tickets_assigned = models.IntegerField(default=0)


class Ticket(models.Model):
    name = models.CharField(max_length=20)
    sbu_id = models.IntegerField()
    location = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    details = models.CharField(max_length=100)
    time_stamp = models.DateTimeField('date submitted')
    ticket_assigned = models.BooleanField(default=False)
    ticket_assigned_to = models.CharField(max_length=20, unique=False, default="admin")



