# core/forms/task_form.py
from django import forms
from core.models import Task
from core.mixins.title_validation_mixin import TitleValidationMixin

class TaskForm(forms.ModelForm, TitleValidationMixin):
    class Meta:
        model = Task
        fields = ['title', 'done']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return self.validate_title(title, instance=self.instance)

