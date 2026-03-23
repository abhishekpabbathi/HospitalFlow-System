from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard.role_views import doctor_dashboard, treat_patient, discharge_patient, receptionist_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('chatbot/', include('chatbot.urls')),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('doctor/treat/<int:patient_id>/', treat_patient, name='treat_patient'),
    path('doctor/discharge/<int:patient_id>/', discharge_patient, name='discharge_patient'),
    path('reception/', receptionist_view, name='receptionist'),
    path('', include('dashboard.urls')),
]
