from django import forms
from educat.models import Groupe

class CreerGroupestForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['name', 'description', 'max_inscription']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Nom de l’enseignant...'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Ajouter une description...', 'rows': 3}),
            'max_inscription': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Nombre maximum d’inscriptions'}),
        }