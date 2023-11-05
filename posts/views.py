from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

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