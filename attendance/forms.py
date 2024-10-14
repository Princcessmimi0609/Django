from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['name', 'category', 'email_address', 'meeting', 'remarks', 'attended', 'date_of_meeting']
        labels = {
            'name': 'Name',
            'category': 'Category',
            'email_address': 'Email',
            'meeting': 'Meeting',
            'remarks': 'Remarks',
            'attended': 'Attended',
            'date_of_meeting': 'Date of Meeting',
        }
        widgets = {
            'name': forms.SelectMultiple(),
            'category': forms.SelectMultiple(),
            'meeting': forms.SelectMultiple(),
            'attended': forms.RadioSelect(),
            'date_of_meeting': forms.DateInput(attrs={'type': 'date'}),
        }
