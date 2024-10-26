from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import post_form
from post import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView

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


# class based create view

class view_addPost(CreateView):
    model=models.Post
    form_class=post_form
    template_name='post.html'
    success_url=reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


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


class edit_post(UpdateView):
        model=models.Post
        form_class=post_form
        template_name='post.html'
        success_url=reverse_lazy('home')
        pk_url_kwarg = 'id'
        
@login_required
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)   
    post.delete()
    return  redirect('home')  


class delete_post(DeleteView):
        model=models.Post
        template_name='delete.html'
        success_url=reverse_lazy('home')
        pk_url_kwarg = 'id'