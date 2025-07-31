"""Serializers do app core para o model Task."""
from rest_framework import serializers
from core.models import Task

# pylint: disable=too-few-public-methods
class TaskSerializer(serializers.ModelSerializer):
    """
    Princípio I (Segregação de Interface - ISP):
    Este serializer define uma interface enxuta para o modelo Task,
    mostrando apenas os campos necessários para a API e ocultando outros
    atributos do modelo que não são tão relevantes para esta camada
    """

    class Meta:
        """Define os campos e configurações do serializer."""
        model = Task
        fields = ['id', 'title', 'done', 'created_at']
        read_only_fields = ['id', 'created_at']
