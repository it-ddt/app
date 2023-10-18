from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return render(request, 'app/index.html')


def greet(request):
    user_name = request.GET['user_name']
    context = {
        'user_name': user_name
    }
    return render(request, 'app/greet.html', context)
