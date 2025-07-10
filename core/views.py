"""Views para gerenciamento das tarefas no app core."""

# pylint: disable=unused-import, too-many-ancestors, relative-beyond-top-level
import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet para API REST das tarefas.

    Fornece CRUD completo para o model Task.
    Apenas usuários autenticados podem acessar.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Usar UUID como campo de lookup na URL
    lookup_field = 'id'
    lookup_value_regex = r'[0-9a-f\-]{36}'

    def get_queryset(self):
        """Retorna apenas as tarefas pertencentes ao usuário autenticado."""
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Salva a nova tarefa associando ao usuário autenticado."""
        serializer.save(owner=self.request.user)

@login_required
def home(request):
    """
    View para página inicial.

    Exibe a lista de tarefas do usuário autenticado, ordenadas por criação mais recente.
    """
    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'core/home.html', {'tasks': tasks})

@login_required
def task_create(request):
    """
    View para criação de nova tarefa.

    Exibe o formulário e salva a tarefa após submissão válida.
    Associa a tarefa ao usuário autenticado.
    """
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
    """
    View para edição de tarefa existente.

    Permite edição apenas para o dono da tarefa ou superusuário.
    Exibe formulário com dados atuais e salva alterações.
    """
    if request.user.is_superuser:
        task = get_object_or_404(Task, pk=pk)
    else:
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
    """
    View para exclusão de tarefa.

    Permite exclusão apenas para o dono da tarefa ou superusuário.
    Confirma exclusão antes de remover.
    """
    if request.user.is_superuser:
        task = get_object_or_404(Task, pk=pk)
    else:
        task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'core/task_confirm_delete.html', {'task': task})

class NotificationAPIView(APIView):
    """View para enviar notificação por e-mail ao acessar a API."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Envia um e-mail para o usuário autenticado."""
        user_email = request.user.email
        if not user_email:
            return Response({"error": "Usuário não possui email cadastrado."}, status=400)

        send_mail(
            'Notificação de acesso à API',
            'Olá! Você acessou a API com sucesso.',
            'debora.costa22396@alunos.ufersa.edu.br',
            [user_email],
            fail_silently=False,
        )

        return Response({"message": f"E-mail enviado com sucesso para {user_email}"})