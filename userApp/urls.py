from . import views
from django.urls import path
from django.contrib.auth import views as log_views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("login/", log_views.LoginView.as_view(template_name="user/login.html"), name="login")
]