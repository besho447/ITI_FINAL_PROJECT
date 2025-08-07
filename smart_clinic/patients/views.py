from django.shortcuts import render, redirect
from .models import Patient
from django.contrib import messages

def patient_profile(request):
    try:
        patient = Patient.objects.get(user=request.user)
        return render(request, 'patients/profile.html', {'patient': patient})
    except Patient.DoesNotExist:
        messages.error(request, "No patient profile found. Please contact an administrator.")
        return redirect('dashboard')
    
