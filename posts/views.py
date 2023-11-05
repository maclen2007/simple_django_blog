from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.http import HttpResponseRedirect

from .models import Post, User

paginator_pages = 1

def index(request):
  latest = Post.objects.order_by('-pub_date')
  paginator = Paginator(latest, paginator_pages)
  page = paginator.get_page(request.GET.get('page'))
  return render(request, "index.html", {"page": page})

def post_view(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  context = {
    'post': post,
  }
  return render(request, 'post.html', context)

def profile(request, username):
  author = get_object_or_404(User, username=username)
  posts = author.posts.all()
  paginator = Paginator(posts, paginator_pages)
  page = paginator.get_page(request.GET.get('page'))
  status = None
  if request.user.is_authenticated:
    status = "Пользователь авторизован"
    context = {
      'author': author,
      'page': page,
      'status': status,
    }
    return render(request, 'profile.html', context)
  
@login_required
def new_post(request):
  form = PostForm(request.POST or None, files=request.FILES or None)
  if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('posts:index')

  context = {
    'header': 'Добавить запись',
    'submit_text': 'Добавить',
    'form': form,
  }

  return render(request, 'new_post.html', context)

def post_edit(request, username, post_id):
  if request.user.username != username:
    return redirect('posts:post', username, post_id)

  post = get_object_or_404(Post, author__username=username, id=post_id)
  form = PostForm(
    request.POST or None, files=request.FILES or None, instance=post
  )
  if form.is_valid():
    post = form.save(commit=False)
    post.save()
    return redirect('posts:post', post_id)

  context = {
    'header': 'Редактировать запись',
    'submit_text': 'Сохранить',
    'form': form,
    'post': post,
  }
  
  return render(request, 'new_post.html', context)

def post_delete(request, username, post_id):
  if request.user.username != username:
    return redirect('posts:post', username, post_id)
  post = get_object_or_404(Post, author__username=username, id=post_id)
  post.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))