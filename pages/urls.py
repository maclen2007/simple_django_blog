from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
  path('about/', views.AboutPagesView.as_view(), name='about'),
]