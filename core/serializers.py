from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # Aqui você pode customizar qualquer campo se quiser (opcional)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'done', 'created_at']
        read_only_fields = ['id', 'created_at']
