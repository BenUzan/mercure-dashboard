from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from accounts.forms import SignupForm
from accounts.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def signupaccount(request):
    template = 'accounts\signup.html'
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            #* Username Existance verfifcation
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Cet utilistaeur existe.'
                } )
            #* Email Existance Verification
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Cet email existe.'
                } )
            #* Password verification
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Les mots de passe ne correspondent pas.'
                } )
            else:
                un = request.POST.get('username_test')
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                    )
                
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                
                user.save()
                login(request, user)
                return redirect('home')
    else:
        form = SignupForm()
    
    return render(request, template, {"form": form})


def loginaccount(request):
    template = 'accounts\login.html'
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                )
            
            if user is None:
                return render(request,template,{
                    'form': form,
                    'error_message': 'username and password do not match'
                })
            else:
                login(request, user)
                return redirect('home')
            
    else:
        form = LoginForm()
            
    return render(request, template, {"form" : form})


def logoutaccount(request):
    return render(request, 'accounts\logout.html')
    