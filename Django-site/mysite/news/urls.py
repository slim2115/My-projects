# Импорт файлов:

from django.urls import path, include

from django.views.generic import ListView 
from django.views.generic import DetailView
from news.models import Articles

# Обработчик для ссылок:
urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    path('(<pk>\d+)', DetailView.as_view(model = Articles, template_name = "news/post.html"))

]
