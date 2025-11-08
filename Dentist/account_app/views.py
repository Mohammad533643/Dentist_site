from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, update_session_auth_hash
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "account/sign_up.html"
    success_url = "dentist_info_app:Home"

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f"welcome {user.username}")
        login(self.request, user)
        return redirect(self.success_url)


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = "account/login.html"

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"welcome {user.username}")
        login(self.request, user)
        return redirect("dentist_info_app:Home")

    def form_invalid(self):
        messages.error(self.request, "There is an error,please try again.")
        return redirect("account_app:Login")


class Change_Password(PasswordChangeView):
    template_name = "account/change_password.html"
    success_url = reverse_lazy("dentist_info_app:Home")

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, "Your password changed successful.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There is an error,please try again.")
        return super().form_invalid(form)


class Logout(LogoutView):
    next_page = "dentist_info_app:Home"
