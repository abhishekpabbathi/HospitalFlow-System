from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'severity', 'department', 'is_resolved', 'created_at']
    list_filter = ['severity', 'is_resolved']
