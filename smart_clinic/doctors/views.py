from django.shortcuts import render, redirect
from .models import Doctor, Schedule
from django.contrib import messages

def doctor_schedule(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
        schedules = Schedule.objects.filter(doctor=doctor)
        return render(request, 'doctors/schedule.html', {'schedules': schedules})
    except Doctor.DoesNotExist:
        messages.error(request, "No doctor profile found. Please contact an administrator.")
        return redirect('dashboard')