from django.shortcuts import render, redirect
from .employee_form import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import EmployeeModel
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# access to authenticated users
@login_required
def employee_create(request, template_name='employeeApp/employee.html'):
    # instantiate a form object
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee Added Successfully")        
        # redirect to same page
        return redirect('employee_create')
    return render(request, template_name, {'form': form})

# employees view
class EmployeeList(LoginRequiredMixin, ListView):
    model = EmployeeModel
    context_object_name = 'employees'
    template_name = "employeeApp/employees.html"
    ordering = ['first_name']

# employee profile
class EmployeeDetail(DetailView):
    model = EmployeeModel
    template_name = "employeeApp/each_employee.html"
    context_object_name = "get_emp_data"
    