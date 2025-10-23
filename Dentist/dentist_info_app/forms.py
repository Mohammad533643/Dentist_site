from django import forms
from .models import Booking, Contact
from datetime import datetime, timedelta


class Booking_Form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Gmail', 'Dentist', 'Date_booking']
        widgets = {
            'Date_booking': forms.DateInput(attrs={"type": "datetime-local",
                                                   "min": (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%dT10:00"),
                                                   "max": (datetime.today() + timedelta(days=2)).strftime("%Y-%m-%dT20:00"),
                                                   "step": 1200,
                                                   }),

            'Gmail': forms.EmailInput(attrs={"class": "form-control"}),
            'Dentist': forms.Select(attrs={"class": "form-control"}),
        }


class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["Gmail", "Message"]
        widgets = {
            "Gmail": forms.EmailInput(attrs={"class": "gmail-field"}),
            "Message": forms.Textarea(attrs={"class": "message-field"})
        }
