from django.views.generic.base import TemplateView

class AboutPagesView(TemplateView):
  template_name = 'pages/about.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'О компании'
    context['text'] = 'Текст странички'
    return context