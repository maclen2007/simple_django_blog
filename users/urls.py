from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
  path("signup/", views.SignUp.as_view(success_url=reverse_lazy('index')), name="signup"),
]