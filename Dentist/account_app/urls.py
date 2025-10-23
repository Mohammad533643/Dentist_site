from django.urls import path
from .views import SignUp, Login, Logout, Change_Password


app_name = "account_app"
urlpatterns = [
    path("sign_up/", SignUp.as_view(), name="Signup"),
    path("login/", Login.as_view(), name="Login"),
    path("Change_password/", Change_Password.as_view(), name="Change_password"),
    path("logout/", Logout.as_view(), name="Logout"),
]
