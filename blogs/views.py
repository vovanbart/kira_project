from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    posts = BlogPost.objects.all()
    return render(request, "blogs/index.html", {"posts": posts})

@login_required
def post_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    else:
        form = BlogPostForm()
    return render(request, "blogs/post_form.html", {"form": form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    else:
        form = BlogPostForm(instance=post)
    return render(request, "blogs/post_form.html", {"form": form, "post": post})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "blogs/register.html", {"form": form})