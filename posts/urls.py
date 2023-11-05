from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
  path("", views.index, name="index"),
  path("<int:post_id>/", views.post_view, name="post"),
  path("<str:username>/", views.profile, name="profile"),
]