
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from Jobs.forms import *
from Jobs.models import UserProfile

def registration_view(request):
    form = RegistrationForm()
    context={
        
    }
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            # Create UserProfile based on user type
            user_type = form.cleaned_data['user_type']
            if user_type == 'employer':
                UserProfile.objects.create(user=user, is_employer=True)
                return redirect('employer')  # Replace with your employee registration success URL
            elif user_type == 'applicant':
                UserProfile.objects.create(user=user, is_applicant=True)
                return redirect('dashboard')  # Replace with your applicant registration success URL
        else:
           context['registration_form']=form
    return render(request, 'register.html', {'form': form})



def login_view(request):
    user=request.user
    context={
        
    }
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect('login')
        else:
            context['login_form']=form
    return render(request,'login.html',context)



def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
def employer_dashboard(request):
    return render(request, 'emp_dashboard.html')
