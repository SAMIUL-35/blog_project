from django.shortcuts import render, redirect
from .form import post_form

def add_post(request):
    if request.method == 'POST':
        p_form = post_form(request.POST)
        if p_form.is_valid():
            print(p_form.cleaned_data)
            p_form.save()  
            return redirect('add_profile')  
    else:
        p_form = post_form()

    return render(request, 'profile.html', {'form': p_form})
