from django.db import models

# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=20)
    sbu_id = models.IntegerField()
    location = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    details = models.CharField(max_length=100)
    time_stamp = models.DateTimeField('date submitted')
    ticket_assigned = models.BooleanField(default=False)
    ticket_assigned_to = models.CharField(max_length=20)


class Employee(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    tickets_assigned = models.ForeignKey(Ticket, on_delete=models.CASCADE)
