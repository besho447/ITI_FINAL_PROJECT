from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('confirmation/', lambda request: render(request, 'appointments/confirmation.html'), name='appointment_confirmation'),
]