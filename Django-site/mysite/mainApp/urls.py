# Импорт файлов:

from . import views
from django.urls import path, include
# Use `django.urls` unstead of `django.conf.urls`
# https://groups.google.com/forum/#!msg/django-users/Z0P6FXPONXI/AXQ1Q2UnBQAJ

# Обработчик для ссылок:

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
