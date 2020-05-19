from django.urls import path
from .import views

urlpatterns = [
    path('', views.employee_create, name='employee_create'),
    path("employees/", views.EmployeeList.as_view(), name="employee_view"),
    path("<int:pk>", views.EmployeeDetail.as_view(), name="employee_one"),
]
