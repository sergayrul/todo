from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo

# Получение данных из БД
def homepage(request):
    todos = Todo.objects.all()
    return  render(request, "index.html", {'todos':todos})

# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')