from django.shortcuts import render, redirect
from .form import author_form  
def add_author(request):
    if request.method == 'POST':
        auth_form = author_form(request.POST)
        if auth_form.is_valid():
            print(auth_form.cleaned_data)
            auth_form.save()  
            return redirect('add_author')  
    else:
        auth_form = author_form()

    return render(request, 'author.html', {'form': auth_form})
