from django.contrib import admin
from .models import Dentist, Booking, Contact
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Dentist, Feature)
# admin.site.register(Booking)
# admin.site.register(Contact)

@admin.register(Dentist)
class Dentist(ImportExportModelAdmin):
    list_display = ["Full_name", "User_id"]
    list_filter = ["Full_name", "User_id"]
    search_fields = ["Full_name", "User_id", "Speciality", "Experience"]


@admin.register(Booking)
class Booking(ImportExportModelAdmin):
    list_display = ["Date_now", "Date_booking", "Appointment_ID"]
    list_filter = ["Patient"]
    search_fields = ["Date_now", "Date_booking",
                     "Appointment_ID", "Patient__username", "Gmail"]


@admin.register(Contact)
class Contact(ImportExportModelAdmin):
    list_display = ["Gmail", "Author"]
    list_filter = ["Author"]
    search_fields = ["Gmail", "Author__username", "Message"]
