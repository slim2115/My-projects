from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_mysite(request):
    return redirect('mainApp', permanent = True)