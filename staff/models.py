from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    ROLE_CHOICES = [('doctor', 'Doctor'), ('nurse', 'Nurse'), ('admin', 'Admin'), ('receptionist', 'Receptionist')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=50)
    on_duty = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.role})'
