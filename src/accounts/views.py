from django.shortcuts import render
from accounts.forms import SignupForm
# Create your views here.

def signupaccount(request):
    form = SignupForm()
    
    return render(request, 'accounts\signupaccount.html', {"form": form})

def loginaccount(request):
    return render(request, 'accounts\loginaccount.html')

def logoutaccount(request):
    return render(request, 'accounts\logoutaccount.html')
    