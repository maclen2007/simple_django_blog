from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post

def index(request):
    latest = Post.objects.order_by('-pub_date')[:10]
    return render(request, "index.html", {"posts": latest})

def post_view(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  context = {
    'post': post,
  }
  return render(request, 'post.html', context)