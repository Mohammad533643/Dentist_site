from django.views.generic import TemplateView
from .seializers import Dentist_Serializer, User_Serializer, Contact_serializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .forms import Booking_Form, Contact_Form
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dentist, Contact


class Home(TemplateView):
    template_name = "dentist_info/home.html"


class Contact_save(LoginRequiredMixin, FormView):
    template_name = "dentist_info/contact.html"
    form_class = Contact_Form

    def form_valid(self, form):
        form = form.save(commit=False)
        form.Author = self.request.user
        form.save()
        return redirect("dentist_info_app:home")

    def form_invalid(self, form):
        return super().form_invalid(form)


class Book(LoginRequiredMixin, FormView):
    template_name = "dentist_info/booking.html"
    form_class = Booking_Form

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.Patient = self.request.user
        booking.save()
        return redirect("dentist_info_app:home")

    def form_invalid(self, form):
        return super().form_invalid(form)


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
