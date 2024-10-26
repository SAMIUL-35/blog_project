from django.shortcuts import render, redirect
from .form import category_form

def add_category(request):
    if request.method == 'POST':
        cat_form = category_form(request.POST)
        if cat_form.is_valid():
            print(cat_form.cleaned_data)
            cat_form.save()  
            return redirect('add_category')  
    else:
        cat_form = category_form()

    return render(request, 'category.html', {'form': cat_form})



