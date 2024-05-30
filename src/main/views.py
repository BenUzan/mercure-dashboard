from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name_x = "ben"
    return render(request, 'main\index.html')

def rapport(request):
    return render(request, "main\\rapport.html")
    
