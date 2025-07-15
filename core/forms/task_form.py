# core/forms/task_form.py
from django import forms
from core.models import Task
from core.mixins.title_validation_mixin import TitleValidationMixin

class TaskForm(forms.ModelForm, TitleValidationMixin):
    """
    Princípio L (Substituição de Liskov - LSP):
    Podemos substituir o uso da ModelForm base pela TaskForm sem quebrar funcionalidades,
    pois a herança respeita o comportamento esperado da classe mãe (ModelForm).
    
    """
    class Meta:
        model = Task
        fields = ['title', 'done']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return self.validate_title(title, instance=self.instance)

