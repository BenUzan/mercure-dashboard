from django.shortcuts import render

# Create your views here.

def signupaccount(request):
    return render(request, 'signupaccount.html')

def loginaccount(request):
    return render(request, 'loginaccount.html')

def logoutaccount(request):
    return render(request, 'logoutaccount.html')
    