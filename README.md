# HospitalFlow System

A real-time hospital operations dashboard inspired by SOPEONOW.

## Built With
- Python + Django
- HTML + CSS + JavaScript
- Groq AI (LLaMA) for chatbot
- SQLite database

## Features
- Real-time patient flow monitoring
- Zone tracking (Red / Yellow / Green)
- Auto alerts when wait time exceeds threshold
- AI chatbot that reads live hospital data
- Role-based access — Admin, Doctor, Receptionist
- Dark / Light mode
- Mobile responsive

## How to Run
`ash
git clone https://github.com/YOUR_USERNAME/hospital-ops-dashboard.git
cd hospital-ops-dashboard
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
`

