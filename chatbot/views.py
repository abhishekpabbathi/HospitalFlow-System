import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from groq import Groq
from patients.models import Patient
from alerts.models import Alert
from staff.models import Staff

client = Groq(api_key=os.environ.get('GROQ_API_KEY', ''))

@csrf_exempt
def ask_chatbot(request):
    if request.method != 'POST':
        return JsonResponse({'reply': 'Invalid request'})
    
    data = json.loads(request.body)
    user_message = data.get('message', '')

    # Build live hospital context
    patients = Patient.objects.exclude(status='discharged')
    alerts = Alert.objects.filter(is_resolved=False)
    staff = Staff.objects.filter(on_duty=True)

    context = f'''You are a hospital operations AI assistant for Hospital Ops dashboard.
Current live hospital data:
PATIENTS ({patients.count()} active):
{chr(10).join([f'- {p.name}, Age {p.age}, Zone: {p.zone.upper()}, Dept: {p.department}, Wait: {p.wait_minutes()} mins, Status: {p.status}' for p in patients])}

ACTIVE ALERTS ({alerts.count()}):
{chr(10).join([f'- {a.title} | {a.department} | Severity: {a.severity.upper()}' for a in alerts])}

STAFF ON DUTY ({staff.count()}):
{chr(10).join([f'- {s.name} | {s.role} | {s.department}' for s in staff])}

Answer questions about current hospital status. Format responses in clean key-value style like "Name: John, Zone: Red, Wait: 30 mins". Each patient or item on a new line. No emojis, no bold text, no markdown. If user says hi, hello, hlo, hey or any greeting, respond with "Hello! How can I assist you today? You can ask me about patients, alerts, staff or hospital status." Keep responses clean and professional.'''

    try:
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[
                {'role': 'system', 'content': context},
                {'role': 'user', 'content': user_message}
            ],
            max_tokens=300
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f'AI service error: {str(e)}'

    return JsonResponse({'reply': reply})
