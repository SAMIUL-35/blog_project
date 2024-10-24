from django.shortcuts import render, redirect
from .form import post_form
from post import models
from django.contrib.auth.decorators import login_required

@login_required
def add_post(request):
    if request.method == 'POST':
        p_form = post_form(request.POST)
        if p_form.is_valid():
            print(p_form.cleaned_data)
            p_form.instance.author=request.user
            p_form.save()  
            return redirect('home')  
    else:
        p_form = post_form()

    return render(request, 'post.html', {'form': p_form})

@login_required
def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    p_form = post_form(instance=post)

    if request.method == 'POST':
        p_form = post_form(request.POST,instance=post)
        if p_form.is_valid():
            print(p_form.cleaned_data)
            p_form.instance.author=request.user
            p_form.save()  
            return redirect('home')  
    

    return render(request, 'post.html', {'form': p_form})

@login_required
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    

    post.delete()
    return  redirect('home')  