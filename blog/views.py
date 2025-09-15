from django.shortcuts import render, redirect
from .form import PostForm

from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{"posts":posts})

def details(request, pk):
    posts = Post.objects.filter(pk=pk)
    return render(request, 'blog/detail.html',{"posts":posts})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'blog/post_edit.html', {"form":form})