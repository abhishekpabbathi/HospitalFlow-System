from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from alerts.models import Alert
from staff.models import Staff

@login_required
def doctor_dashboard(request):
    try:
        staff = Staff.objects.get(user=request.user)
    except Staff.DoesNotExist:
        return redirect('/')
    my_patients = Patient.objects.filter(department=staff.department).exclude(status='discharged').order_by('-registered_at')
    waiting_count = my_patients.filter(status='waiting').count()
    dept_alerts = Alert.objects.filter(department=staff.department, is_resolved=False)
    return render(request, 'doctor.html', {
        'staff': staff,
        'my_patients': my_patients,
        'waiting_count': waiting_count,
        'dept_alerts': dept_alerts,
    })

@login_required
def treat_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.status = 'in_treatment'
    patient.save()
    return redirect('doctor_dashboard')

@login_required
def discharge_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.status = 'discharged'
    patient.save()
    return redirect('doctor_dashboard')

@login_required
def receptionist_view(request):
    success = False
    if request.method == 'POST':
        Patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            department=request.POST['department'],
            zone=request.POST['zone'],
            status='waiting'
        )
        success = True
    patients = Patient.objects.exclude(status='discharged').order_by('-registered_at')
    return render(request, 'receptionist.html', {'patients': patients, 'success': success})
