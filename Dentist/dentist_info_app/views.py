from django.views.generic import TemplateView

# rigeon: api

from .seializers import Dentist_Serializer, User_Serializer, Contact_serializer
from rest_framework.viewsets import ModelViewSet

# endrigeon

from django.contrib.auth.models import User

# region:register

from .forms import Booking_Form, Contact_Form
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# endrigeon

from .models import Dentist, Contact, Booking
from django.contrib import messages
from django.db.models import Q
from django.views.generic import View
from django.shortcuts import render


class Home(TemplateView):
    template_name = "dentist_info/home.html"


class Search(View):
    def get(self, request):
        inp = request.GET.get("query")
        query = Dentist.objects.filter(Q(Full_name__icontains=inp) | Q(User_id=inp) |
                                       Q(Speciality__icontains=inp) | Q(City__icontains=inp) |
                                       Q(Experience__icontains=inp)
                                       )
        context = {"query": query}
        return render(request, "dentist_info/search.html", context)


class Contact_save(LoginRequiredMixin, FormView):
    template_name = "dentist_info/contact.html"
    form_class = Contact_Form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.Author = self.request.user
        obj.save()
        return redirect("dentist_info_app:Home")

    def form_invalid(self, form):
        return super().form_invalid(form)


class Book(LoginRequiredMixin, FormView):
    template_name = "dentist_info/booking.html"
    form_class = Booking_Form

    def form_valid(self, form):
        # getting dentist name and time of booking from request
        dentist_name_in_request = self.request.POST.get("Dentist")
        booking_time = self.request.POST.get("Date_booking")

        # getting reserved dentist's names and reserved times of booking from Booking model in database
        reserved_dentists = Booking.objects.all().values_list("Dentist")
        reserved_times = Booking.objects.all().values_list("Date_booking")

        # Checking time and the requested dentist for booking to avoid conflicts
        if dentist_name_in_request in reserved_dentists:
            if not (booking_time in reserved_times):
                booking = form.save(commit=False)
                booking.Patient = self.request.user
                booking.save()
                return redirect("dentist_info_app:Home")
        else:
            booking = form.save(commit=False)
            booking.Patient = self.request.user
            booking.save()
            return redirect("dentist_info_app:Home")

        messages.error(
            self.request, "Change the time's visit or drntist Please.")
        return redirect("dentist_info_app:Booking")

    def form_invalid(self, form):
        return super().form_invalid(form)


class Appointment_list(TemplateView):
    template_name = "dentist_info/user_appointments.html"
    model = Booking.objects.all()

    def get_context_data(self):
        context = super().get_context_data()
        context["appointments"] = Booking.objects.filter(
            Patient=self.request.user)
        return context


class Dentists_list(TemplateView):
    template_name = "dentist_info/dentists.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["Dentist"] = Dentist.objects.all()
        return context


class Dentist_api(ModelViewSet):
    serializer_class = Dentist_Serializer
    queryset = Dentist.objects.all()


class Contact_api(ModelViewSet):
    serializer_class = Contact_serializer
    queryset = Contact.objects.all()


class User_api(ModelViewSet):
    serializer_class = User_Serializer
    queryset = User.objects.all()
