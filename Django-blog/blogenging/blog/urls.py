# Импорт позиционного аргумента "path", "include".
from django.urls import path, include
# Импорт всего (*) что есть по адресу текущего каталога blog/views.  
from .views import *


# http://localhost:5000/blog/some-title

# urlpatterns - переменная в роли списка.
# posts_list - функция обрабатывающая запрос.
urlpatterns = [
    path('', posts_list),
    
]