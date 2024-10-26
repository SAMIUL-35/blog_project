from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import RegisterForm,ChangeUserForm 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.views import LoginView
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


class user_login(LoginView):
    template_name='register.html'
    # success_url=reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
    
        messages.success(self.request,'login succesful')
        return super().form_valid(form)
    def form_invalid(self, form):
    
        messages.success(self.request,'login unsuccesful')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[type]='login'
        return context
    
@login_required
def profile(request): 
      data = Post.objects.filter(author=request.user) 
      return render(request, 'profile.html', {'data':data})
@login_required
def edit_profile(request):
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

    return render(request, 'update_profile.html', {'form': profile_form, })


def User_logout(request):
    logout(request)
    return redirect('home')
@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)  # ensure correct order
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Password changed successfully')  # Fixed typo
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_pass.html', {'form': form})
