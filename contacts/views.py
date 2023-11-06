from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

# Create your views here.

def contact_view(request):
  if request.method == 'GET':
    form = ContactForm()
  elif request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      from_email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      try:
        send_mail(f'Пришла заявка от пользователя с email: {from_email}', message,
        settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
      except BadHeaderError:
        return HttpResponse('Ошибка в теме письма.')
      return redirect('success')
    else:
      return HttpResponse('Неверный запрос.')
  return render(request, "email.html", {'form': form})

def success_view(request):
  return render(request, "success.html")
