from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.contrib.auth.models import User
import random


class Dentist(models.Model):
    Full_name = models.CharField(max_length=200)
    User_id = models.CharField(
        validators=[MinLengthValidator(6)], max_length=6, unique=True)
    Speciality = models.CharField(max_length=20)
    Experience = models.TextField(max_length=1000, blank=True, null=True)
    Profile_img = models.ImageField(
        upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.Full_name


class Booking(models.Model):
    def Generate_appointment_id():
        return random.randint(100000, 999999)
    Patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Booking_history")
    Gmail = models.EmailField(max_length=250)
    Dentist = models.ForeignKey(
        Dentist, on_delete=models.CASCADE, related_name="Dentist_info")
    Date_now = models.DateTimeField(default=timezone.now)
    Date_booking = models.DateTimeField()
    Appointment_ID = models.CharField(
        max_length=10, unique=True, default=Generate_appointment_id)

    def __str__(self):
        return self.Appointment_ID


class Contact(models.Model):
    Author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contact_messages")
    Date_now = models.DateTimeField(default=timezone.now)
    Gmail = models.EmailField()
    Message = models.TextField()
