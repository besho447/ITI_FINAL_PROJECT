from django.db import models
from doctors.models import Doctor, Schedule
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')), default='pending')

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.schedule.date}"