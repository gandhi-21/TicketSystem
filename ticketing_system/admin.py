from django.contrib import admin


from .models import Ticket, Employee
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Employee)


