from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.

def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task': task1})


def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    task2=Task.objects.get(id=id)
    form=TaskForm(request.POST or None, instance=task2)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html',{'task':task2,'form':form})
