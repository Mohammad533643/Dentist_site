from django.contrib import admin
from .models import Dentist, Booking, Contact
from import_export.admin import ImportExportModelAdmin


class Feature(admin.ModelAdmin):
    list_display = ["Full_name", "User_id"]
    list_filter = ["Full_name", "User_id"]
    search_fields = ["Full_name", "User_id", "Speciality", "Experience"]


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
    pass


@admin.register(Contact)
class Contact(ImportExportModelAdmin):
    pass
