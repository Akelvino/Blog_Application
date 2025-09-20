from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{"posts":posts})

def details(request, pk):
    posts = Post.objects.filter(pk=pk)
    return render(request, 'blog/detail.html',{"posts":posts})
