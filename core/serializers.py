"""Serializers do app core para o model Task."""

from rest_framework import serializers
from core.models import Task

# pylint: disable=too-few-public-methods
class TaskSerializer(serializers.ModelSerializer):
    """Serializer para o model Task."""

    class Meta:
        """Define os campos e configurações do serializer."""
        model = Task
        fields = ['id', 'title', 'done', 'created_at']
        read_only_fields = ['id', 'created_at']
