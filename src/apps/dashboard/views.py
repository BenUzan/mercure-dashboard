from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def start(request):
    template = 'dashboard\start.html'
    return render(request, template)


@login_required(login_url="/login")
def dashboard(request):
    template = 'dashboard\dashboard.html'
    return render(request, template)
