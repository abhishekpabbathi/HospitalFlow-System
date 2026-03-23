
from django.db import models

class Alert(models.Model):
    SEVERITY = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    title = models.CharField(max_length=200)
    message = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY, default='medium')
    department = models.CharField(max_length=50)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title