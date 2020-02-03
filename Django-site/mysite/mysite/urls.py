"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Импорт файлов:

from django.contrib import admin
from django.urls import path, include
# Use `django.urls` unstead of `django.conf.urls`
# https://groups.google.com/forum/#!msg/django-users/Z0P6FXPONXI/AXQ1Q2UnBQAJ

#from .views import redirect_mysite

# Обработчик для ссылок:

urlpatterns = [
    #path('', redirect_mysite),
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('', include('mainApp.urls')),
    path('news/', include('news.urls')),
]
