from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from doctors.models import Schedule
from patients.models import Patient

@login_required
def book_appointment(request):
    if request.method == 'POST':
        schedule_id = request.POST.get('schedule_id')
        reason = request.POST.get('reason')
        schedule = Schedule.objects.get(id=schedule_id)
        patient = Patient.objects.get(user=request.user)
        Appointment.objects.create(patient=patient, doctor=schedule.doctor, schedule=schedule, reason=reason)
        schedule.is_available = False
        schedule.save()
        return redirect('appointment_confirmation')
    schedules = Schedule.objects.filter(is_available=True)
    return render(request, 'appointments/book.html', {'schedules': schedules})