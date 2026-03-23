from django.db import models

class Patient(models.Model):
    ZONE_CHOICES = [('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green')]
    STATUS_CHOICES = [('waiting', 'Waiting'), ('in_treatment', 'In Treatment'), ('discharged', 'Discharged')]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    zone = models.CharField(max_length=10, choices=ZONE_CHOICES, default='green')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    registered_at = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=50, default='ER')

    def wait_minutes(self):
        from django.utils import timezone
        delta = timezone.now() - self.registered_at
        return int(delta.total_seconds() / 60)

    def __str__(self):
        return self.name
