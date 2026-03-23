from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'zone', 'department', 'status', 'registered_at']
    list_filter = ['zone', 'status', 'department']
    search_fields = ['name']
