# Импорт объектов:
from django.http import HttpResponse
# Возвращает HttpResponseRedirect на соответствующий URL для переданных аргументов.
from django.shortcuts import redirect

def hello(request):
# Определение метода (функции) "hello":
# Возвращает ответ:    
    return HttpResponse('<h1>Hello world</h1>')
    
# Просмотр содержания объекта (request):
"""
print()
    print(request)
    print()
    print(dir(request))
    print()
    pass
"""
