from django.shortcuts import render, redirect
from .form import profile_form

def add_profile(request):
    if request.method == 'POST':
        pro_form = profile_form(request.POST)
        if pro_form.is_valid():
            print(pro_form.cleaned_data)
            pro_form.save()  
            return redirect('add_profile')  
    else:
        pro_form = profile_form()

    return render(request, 'profile.html', {'form': pro_form})
