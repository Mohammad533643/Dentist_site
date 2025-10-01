from django.urls import path
from .views import SignUp, Login, Logout


app_name = "account_app"
urlpatterns = [
    path("sign_up/", SignUp.as_view(), name="Signup"),
    path("login/", Login.as_view(), name="Login"),
    path("logout/", Logout.as_view(), name="Logout"),
]
