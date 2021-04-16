from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import TodoList
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = TodoList.objects.all()
            return redirect('home')

    else:
        all_items = TodoList.objects.all()
        return render(request, 'testform1.html', {'all_items': all_items})


def delete(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.delete()
    return redirect('home')


def cross_off(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.completed = 1
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.completed = 0
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = TodoList.objects.get(pk=list_id)

        form = TodoForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = TodoList.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item':item})



