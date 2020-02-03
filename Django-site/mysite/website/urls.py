# Импорт файлов:

from django.urls import path, include
# Use `django.urls` unstead of `django.conf.urls`
# https://groups.google.com/forum/#!msg/django-users/Z0P6FXPONXI/AXQ1Q2UnBQAJ
from . import views

# Обработчик для ссылок:

urlpatterns = [
    path('', views.index, name='index'),
] 