from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *


def Tasks(request):
    tasks = Todolist.objects.all()
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data.get('task')
            create_task = Todolist(task=new_task)
            create_task.save()
            return redirect("/")
    else:
        form = TodolistForm()

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'task_list.html', context)


def update_task(request, pk):
    task = Todolist.objects.get(id=pk)
    form = TodolistForm(instance=task)
    if request.method == 'POST':
        form = TodolistForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'form': form
    }
    return render(request, "update.html", context)


def remove_from_todolist(request, pk):
    item = get_object_or_404(Todolist, id=pk)
    if item:
        item.delete()
        return redirect("/")
    else:
        return redirect("/")
