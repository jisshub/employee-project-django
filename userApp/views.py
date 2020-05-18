from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

# index view
def index_page(request):
    return render(request, 'userApp/index.html')

# register view
def register_view(request):
    if request.method == "POST":
        # form instance with argument as posted data
        form = UserCreationForm(request.POST)
        if  form.is_valid:
            form.save()
            messages.success(request, "New Account Created")
    else:
        form = UserCreationForm()
    # render the form
    return render(request, 'userApp/register.html', {"reg_form": form})


            
    