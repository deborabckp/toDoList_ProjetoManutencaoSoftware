from django.core.exceptions import ValidationError
from core.models import Task

class TitleValidationMixin:
    """
    Princípio S (Responsabilidade Única - SRP):
    Esta classe tem a responsabilidade única de validar títulos,
    separando a lógica de validação da lógica de formulário.
    
    Princípio D (Inversão de Dependência - DIP):
    Ainda há acoplamento direto com o modelo Task.
    Para aplicar totalmente o DIP, poderíamos injetar a dependência do modelo
    via argumento ou interface, facilitando testes e manutenção.
    
    """
    def validate_title(self, title, instance=None):
        if not title or not title.strip():
            raise ValidationError("O título não pode estar vazio.")
        
        qs = Task.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        
        if qs.exists():
            raise ValidationError("Já existe uma tarefa com esse título.")
        
        return title
