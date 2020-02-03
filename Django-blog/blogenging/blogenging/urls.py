"""blogenging URL Configuration

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
# Импортируемые в "Django" функции 
from django.contrib import admin
from django.urls import path, include

"""
path('blog/', include('blog.urls')),
Определение "hello" в blog/views/ 
from .views import hello

urlpatterns обработчик ссылок принимающий request(запрос) из views(controller в Django).
Функция path может принимать 4 аргумента, 2 из них позиционные, 1 имя паттерна (admin) 
или аргумент обработчика и дополнительные параметры.
Позиционные аргументы: шаблон урла ('/'). 
по которому обрабатывается запрос урла через функцию (path).
Аргумент обработчика, как пример - (admin.site.urls).
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
