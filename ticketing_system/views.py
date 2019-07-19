from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from .models import Ticket, Employee
# Create your views here.


#   Make this the login or submit a ticket page
def index(request):
    return HttpResponse("This is the ticket system homepage.")


#   Make this admin/supervisor login only accessible
def tickets(request):
    tickets_list = get_list_or_404(Ticket, is_active=True)
    return render(request, 'ticketing_system/tickets.html', {'tickets_list': tickets_list})


#   Make this login only accessible
def employee(request):
    response = "You're at the employee dashboard."
    return HttpResponse(response)
