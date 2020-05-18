from django.shortcuts import render

# Create your views here.

# index view
def index_page(request):
    return render(request, 'userApp/index.html')
