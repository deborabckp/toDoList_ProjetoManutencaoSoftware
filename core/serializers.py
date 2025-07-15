"""Serializers do app core para o model Task."""

from rest_framework import serializers
from core.models import Task

# pylint: disable=too-few-public-methods
class TaskSerializer(serializers.ModelSerializer):
    """Serializer para o model Task.

    Princípio I (Segregação de Interface - ISP):
    Este serializer só expõe os campos necessários (id, title, done, created_at),
    evitando depender de métodos ou atributos que não são usados.
    
    """

    class Meta:
        """Define os campos e configurações do serializer."""
        model = Task
        fields = ['id', 'title', 'done', 'created_at']
        read_only_fields = ['id', 'created_at']
