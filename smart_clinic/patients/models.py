from django.db import models
from accounts.models import CustomUser

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'patient'})
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()