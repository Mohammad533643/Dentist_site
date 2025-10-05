from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import redirect


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "account/sign_up.html"
    success_url = "dentist_info_app:Home"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = "account/login.html"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect("dentist_info_app:Home")

    def form_invalid(self, form):
        return redirect("account_app:Login")


class Logout(LogoutView):
    next_page = "dentist_info_app:Home"
