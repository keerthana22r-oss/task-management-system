from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'estimated_hours', 'due_date', 'assigned_to']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Detailed description...'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'estimated_hours': forms.NumberInput(attrs={'step': 0.5, 'min': 0}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].required = False
        self.fields['estimated_hours'].required = False
        self.fields['due_date'].required = False