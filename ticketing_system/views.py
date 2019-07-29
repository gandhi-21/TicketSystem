from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Ticket, Employee

import re
# Create your views here.


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponse('Logged out. Redirect to homepage')


def make_ticket_object(request):
    ticket = Ticket()
    ticket.name = request.POST.get('name', 'Name not given')
    ticket.sbu_id = request.POST.get('sbu_id', 000000000)

    matched = re.match("\d{9}", str(ticket.sbu_id))

    if not matched:
        return 'Wrong sbu id'

    ticket.location = request.POST.get('location', 'Location not given')
    ticket.is_active = True
    ticket.details = request.POST.get('Details', 'Details not given')
    ticket.time_stamp = datetime.datetime.now()
    ticket.ticket_assigned = False
    ticket.ticket_assigned_to = 'Admin'

    return ticket


def make_employee_object(request):
    employee = Employee()
    employee.name = request.POST.get('name', 'Name not given')
    employee.department = request.POST.get('department', 'Department not given')
    employee.user = request.POST.get('username')
    employee.tickets_assigned = 0

    return employee


#   Make this the login or submit a ticket page
def index(request):
    return render(request, 'ticketing_system/index.html')


def tickets(request, employee=None):
    if not request.user.is_authenticated:
        return render(request, 'ticketing_system/employee.html')
    else:
        if employee is not None:
            tickets_list = Ticket(is_active=True, ticket_assigned_to=employee.username)
            return render(request, 'ticketing_system/tickets.html', {'tickets_list': tickets_list})


def employee(request):
    if request.method == 'GET':
        return render(request, 'ticketing_system/employee.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            employee = get_object_or_404(Employee, username=username)
            return tickets(request, employee)
        else:
            return HttpResponse('Wrong username or password. Redirect to login page.')


def create_employee(request):

    if request.method == 'GET':
        return render(request, 'ticketing_system/create_employee.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.get(username__exact=username) is not None:
            return HttpResponse('Not unique username.')

        if User.objects.get(email__exact=email) is not None:
            return HttpResponse('Not unique email.')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        employee = make_employee_object(request)

        employee.save()
        return HttpResponseRedirect('/')


def submit_ticket(request):

    if request.method == 'GET':
        return render(request, 'ticketing_system/submit_ticket.html')
    else:
        ticket = make_ticket_object(request)
        if ticket == 'Wrong sbu id':
            return HttpResponse('Wrong sbu id redirect')
        ticket.save()
        return HttpResponseRedirect('/ticketing_system')
