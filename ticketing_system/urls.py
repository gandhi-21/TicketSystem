from django.urls import path

from . import views


app_name = 'ticketing_system'
urlpatterns = [
    path('', views.index, name='index'),
    path('/tickets', views.tickets, name='tickets'),
    path('/employee/', views.employee, name='employee'),
    path('/employee/new', views.create_employee, name='create_employee'),
    path('/submit_ticket/', views.submit_ticket, name='submit_ticket')
]
