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

        if not post.thread:
            thread_number = Thread.objects.count() + 1
            Thread.objects.get_or_create(thread_number=thread_number)
            post.thread = Thread.objects.get(thread_number=thread_number)
        post.number = post_count + 1
        post.save()
        return redirect('/')
    posts = Post.objects.all()
    return render(request, 'post_list/index.html', {'form': form, 'post_list': posts, 'title': 'Пишите что хотите'})


def thread(request, thread_number):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post_count = Post.objects.all().count()
        post.thread = Thread.objects.get(thread_number=thread_number)
        post.number = post_count + 1
        post.save()
        return redirect('post_list:thread', thread_number=thread_number)
    thread = get_object_or_404(Thread, thread_number=thread_number)
    post_list = thread.thread.select_related('thread')

    return render(request, 'post_list/thread.html', {'form': form, 'post_list':post_list})
