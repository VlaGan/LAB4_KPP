from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def listId(Entity):
    list_id = Entity.objects.values_list('id')
    if not list_id:
        return 0
    return list_id


def index(request):
    # отримуємо список всіх id
    id_list = listId(Task)

    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('main')
        else:
            error = 'Невірний формат!'

    form = TaskForm()
    comments = Task.objects.order_by('-id')
    dictionary = {
        'form': form,
        'error': error,
        'comments': comments,
        'id': id_list
    }

    return render(request, 'main/index.html', dictionary)


def about(request):
    # отримуємо список всіх id
    id_list = listId(Task)
    # отримуємо отсанній id і делейтим всі
    if not id_list == 0:
        if request.method == 'POST':
            last_id = Task.objects.last().id
            for i in range(len(id_list)):
                Task.objects.filter(id=last_id+i).delete()
            return redirect('main')

    return render(request, 'main/about.html')


def add_comment(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save()
            form.clean()
        else:
            error = 'Невірний формат!'


    form = TaskForm()
    comments = Task.objects.order_by('-id')
    dictionary = {
        'form': form,
        'error': error,
        'comments': comments

    }
    return render(request, 'main/comment.html', dictionary)

