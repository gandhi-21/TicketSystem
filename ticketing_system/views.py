from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Ticket, Employee
# Create your views here.


#   Make this the login or submit a ticket page
def index(request):
    return render(request, 'ticketing_system/index.html')


#   Make this admin/supervisor login only accessible
def tickets(request):
    tickets_list = get_list_or_404(Ticket, is_active=True)
    return render(request, 'ticketing_system/tickets.html', {'tickets_list': tickets_list})


#   Login page for employee. Redirects to the dashboard
def employee(request):
    if request.method == 'GET':
        return render(request, 'ticketing_system/employee.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            employee = get_object_or_404(Employee, username=username)
            # tickets = get_list_or_404(Ticket, ticket_assigned_to=employee)
            return HttpResponse('list of all tickets // redirect to the dashboard')
        else:
            return HttpResponse('asdad')


def create_employee(request):

    if request.method == 'GET':
        return render(request, 'ticketing_system/create_employee.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        employee = Employee()
        employee.name = request.POST.get('name', 'Name not given')
        employee.department = request.POST.get('department', 'Department not given')
        employee.user = username
        employee.tickets_assigned = 0
        employee.save()

        return HttpResponseRedirect('/')


def submit_ticket(request):

    if request.method == 'GET':
        return render(request, 'ticketing_system/submit_ticket.html')
    else:
        ticket = Ticket()
        ticket.name = request.POST.get('name', 'Name Not Given')
        ticket.sbu_id = request.POST.get('sbu_id', 00)
        ticket.location = request.POST.get('location', 'Location not Given')
        ticket.is_active = True
        ticket.details = request.POST.get('details', 'Details not given')
        ticket.time_stamp = datetime.datetime.now()
        ticket.ticket_assigned = False
        ticket.ticket_assigned_to = None
        ticket.save()
        return HttpResponseRedirect('/ticketing_system')
