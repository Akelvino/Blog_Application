from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{"posts":posts})

def details(request, pk):
    posts = Post.objects.filter(pk=pk)
    return render(request, 'blog/detail.html',{"posts":posts})

def post_new(request):
    if request.method == 'POST':
        form =PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        
    return render(request, 'blog/post_new.html', {"form":form})