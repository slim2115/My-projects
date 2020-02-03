from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': 
    ['Если у вас остались вопросы то задавайте мне их по телефону', '(068) 068-68-68', 'site.@mail.com']})
# Create your views here.
