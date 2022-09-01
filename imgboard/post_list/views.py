from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Thread
# Create your views here.
from .forms import PostForm


def index(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post_count = Post.objects.all().count()
        post.number = post_count + 1
        post.save()
        return redirect('/')
    posts = Post.objects.all()
    return render(request, 'post_list/index.html', {"form": form, 'post_list': posts, 'title': 'Пишите что хотите'})


def thread(request, slug):
    thread = get_object_or_404(Thread, slug=slug)
    post_list = Thread.objects.all()
    context = {
        'thread': thread,
        'page_obj': post_list,
    }
    return render(request, 'posts/thread.html', context)
