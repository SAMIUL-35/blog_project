from django.shortcuts import render, redirect
from .form import RegisterForm,ChangeUserForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save() 
            messages.warning(request, 'Registration successful') 
            return redirect('login')  
    else:
        register_form = RegisterForm()

    return render(request, 'register.html', {'form': register_form, 'type': 'register'})

def user_login(request):
    if request.method == 'POST':
        log_form = AuthenticationForm(request, request.POST)
        if log_form.is_valid():
            user_name = log_form.cleaned_data['username']
            password = log_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                messages.warning(request, 'Login successful') 
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')  
                return redirect('user_login')  
        else:
            messages.error(request, 'Form is not valid')
            return redirect('register')   
    else:
        log_form = AuthenticationForm()

    
    return render(request, 'register.html', {'form': log_form, 'type': 'login'})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST,instance=user)
        if profile_form.is_valid():
            print(profile_form.cleaned_data)
            profile_form.save() 
            messages.warning(request, 'profile successful') 
            return redirect('profile')  
    else:
        profile_form = ChangeUserForm(instance=user)

    return render(request, 'profile.html', {'form': profile_form, })
