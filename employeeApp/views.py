from django.shortcuts import render, redirect
from .employee_form import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

