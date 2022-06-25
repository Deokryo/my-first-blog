from ast import Is
from multiprocessing import AuthenticationError
from pickle import NONE
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone, timesince
from .models import Post
from .forms import PostForm
from django.contrib import auth
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pulished_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form': form})

def join(request):
    if request.method =='POST':
        if request.POST['password1']== request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password1'],
                email=request.POST['email'])
            auth.login(request, user)
            return redirect('post_list')
    else:
        return render(request, 'user/join.html')

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            render(request,'user/log_in.html')
        else:
            render(request, 'user/log_in.html',{'error':'email or password is incorrect.'})
        
    return render(request, 'user/log_in.html')

           
def log_out(request):
    auth.logout(request)
    return redirect('post_list')




    





# Create your views here.
