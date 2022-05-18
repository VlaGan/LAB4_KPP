from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "comment"]
        widgets = {
            "title": TextInput(
                attrs={
                    'class': 'form-control alert-primary',
                    'placeholder': 'Введіть нікнейм.'
                }),
            "comment": Textarea(attrs={
                'class': 'form-control alert-primary',
                'placeholder': 'Введіть коментар.',
                'rows': '5'
            })
        }
