from django import forms
from .models import Recipe


class AdminRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        