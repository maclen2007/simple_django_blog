from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ("pk", "title_href", "pub_date", "author")
  search_fields = ("text",)
  list_filter = ("pub_date",)

  def title_href(self, obj):
    return format_html('<a href="%s">%s</a>' % (obj.id, obj.title))
  
  title_href.short_description = "Название статьи"

admin.site.register(Post, PostAdmin)