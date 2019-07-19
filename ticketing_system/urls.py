from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/tickets/', views.tickets, name='tickets'),
    path('/employee/', views.employee, name='employee'),
]
