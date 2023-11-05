from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
  path("", views.index, name="index"),
  path("new/", views.new_post, name="new_post"),
  path("<int:post_id>/", views.post_view, name="post"),
  path("<str:username>/", views.profile, name="profile"),
  path("<str:username>/<int:post_id>/edit/", views.post_edit, name="post_edit"),
  path("<str:username>/<int:post_id>/delete/", views.post_delete, name="post_delete"),
]