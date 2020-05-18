from . import views
from django.urls import path
from django.contrib.auth import views as log_views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", log_views.LoginView.as_view(template_name="userApp/login.html"), name="login"),
    path("logout/", log_views.LogoutView.as_view(template_name="userApp/logout.html"), name="logout"),
]

