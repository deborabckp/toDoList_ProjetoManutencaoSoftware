import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class   = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    lookup_field       = 'id'
    lookup_value_regex = r'[0-9a-f\-]{36}'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@login_required
def home(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'core/home.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'core/task_form.html', {'form': form, 'title': 'Criar tarefa'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'core/task_form.html', {'form': form, 'title': 'Editar tarefa'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'core/task_confirm_delete.html', {'task': task})
