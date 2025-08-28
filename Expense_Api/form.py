from django import forms
from .models import ExpensePage

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpensePage
        fields = ['amount', 'description', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }