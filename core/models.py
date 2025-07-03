"""
Modelos do app core: definem as tarefas da aplicação.
"""

import uuid
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Modelo que representa uma tarefa do usuário."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
