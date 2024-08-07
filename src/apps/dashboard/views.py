from django.shortcuts import render

# Create your views here.


def start(request):
    template = 'dashboard\start.html'
    return render(request, template)


def dashboard(request):
    template = 'dashboard\dashboard.html'
    return render(request, template)
