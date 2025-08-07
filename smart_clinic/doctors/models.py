from django.db import models
from accounts.models import CustomUser

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'})
    specialization = models.CharField(max_length=100)
    license_no = models.CharField(max_length=50, unique=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} - {self.date} {self.start_time}-{self.end_time}"