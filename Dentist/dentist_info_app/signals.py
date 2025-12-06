from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Booking

@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, created, **kwars):
    if created:
        subject = f"Appointment information"
        text = f"""
                Hello {instance.Patient.username},
                Your appointment has been booked successfully.

                Appointment ID: {instance.Appointment_ID}
                Dentist: {instance.Dentist}
                Date: {instance.Date_booking}

                Thank you for choosing our clinic!
                """
        html_message = render_to_string("dentist_info/message.html", {
            "booking": instance
        })

        email = EmailMultiAlternatives(
            subject=subject,
            body=text,
            from_email="tesysendingwithpython@gmail.com",
            to=[instance.Gmail],
        )
        email.attach_alternative(html_message, "text/html")
        email.send()
