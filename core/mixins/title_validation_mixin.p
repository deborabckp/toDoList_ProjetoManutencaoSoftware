from django.core.exceptions import ValidationError
from core.models import Task

class TitleValidationMixin:
    """
    Mixin para validar o título de uma tarefa.

    Método:
        validate_title(title: str, instance: Task | None = None) -> str

    Parâmetros:
        title: título a ser validado.
        instance: instância da tarefa em edição (opcional). Se fornecida,
                  será ignorada na verificação de duplicidade para permitir
                  atualização sem erro.

    Validações:
        - Título não pode ser vazio ou só espaços.
        - Título deve ser único, ignorando o objeto em edição e diferenças
          de maiúsculas/minúsculas.
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
