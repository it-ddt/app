from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from datetime import datetime

users = ['Вася Питонов', 'Петя Гадюкин']


def index(request):
    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)


def add(request):
    if request.method == 'GET':
        return render(request, 'app/add.html')
    elif request.method == 'POST':
        user = request.POST.get('user_name', False)
        users.append(user)
        return redirect('index')
    else:
        return HttpResponseNotAllowed(
            ['POST', 'GET'],
            content='Ошибка Этот метод не разрешен!'
        )