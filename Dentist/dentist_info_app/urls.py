from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import Home, Search, Dentist_api, User_api, Contact_api, Dentists_list, Contact_save, Book, Appointment_list
from rest_framework.routers import DefaultRouter

router_1 = DefaultRouter()
router_1.register("", Dentist_api)

router_2 = DefaultRouter()
router_2.register("", User_api)

router_3 = DefaultRouter()
router_3.register("", Contact_api)

app_name = "dentist_info_app"
urlpatterns = [
    path('Home/', Home.as_view(), name="Home"),
    path('Search/', Search.as_view(), name="Search"),
    path('Contact/', Contact_save.as_view(), name="Contact"),
    path('Dentist/', Dentists_list.as_view(), name="Dentist_list"),
    path('Booking/', Book.as_view(), name="Booking"),
    path('MyAppointments/', Appointment_list.as_view(), name="MyAppointments"),
    path('Dentist_api/', include(router_1.urls), name="Dentist_aap"),
    path('User_api/', include(router_2.urls), name="User_api"),
    path('Contact_api/', include(router_3.urls), name="contact_api"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
