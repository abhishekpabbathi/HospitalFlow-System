from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from alerts.models import Alert
from staff.models import Staff
from rest_framework.decorators import api_view
from rest_framework.response import Response

@login_required
def dashboard_view(request):
    patients = Patient.objects.exclude(status='discharged')
    alerts = Alert.objects.filter(is_resolved=False).order_by('-created_at')[:5]
    staff = Staff.objects.filter(on_duty=True)
    context = {
        'patients': patients,
        'alerts': alerts,
        'staff': staff,
        'total_patients': patients.count(),
        'active_alerts': alerts.count(),
        'staff_on_duty': staff.count(),
        'red_zone': patients.filter(zone='red').count(),
    }
    return render(request, 'dashboard.html', context)

@api_view(['GET'])
def live_data(request):
    patients = Patient.objects.exclude(status='discharged')
    alerts = Alert.objects.filter(is_resolved=False)
    patient_data = [{
        'id': p.id,
        'name': p.name,
        'age': p.age,
        'zone': p.zone,
        'status': p.status,
        'department': p.department,
        'wait_minutes': p.wait_minutes(),
    } for p in patients]
    alert_data = [{
        'id': a.id,
        'title': a.title,
        'message': a.message,
        'severity': a.severity,
        'department': a.department,
    } for a in alerts]
    return Response({
        'patients': patient_data,
        'alerts': alert_data,
        'stats': {
            'total': patients.count(),
            'red': patients.filter(zone='red').count(),
            'yellow': patients.filter(zone='yellow').count(),
            'green': patients.filter(zone='green').count(),
            'active_alerts': alerts.count(),
        }
    })
