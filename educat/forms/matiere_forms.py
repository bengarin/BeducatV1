from django import forms
from educat.models import Matiere

class CreerMatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['title', 'code', 'niveau', 'volume_horaire', 'enseignant']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer le titre de la matière...'}),
            'code': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer le code de la matière...'}),
            'niveau': forms.Select(attrs={"class": "form-control"}),
            'volume_horaire': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Entrer le volume horaire...'}),
            'enseignant': forms.Select(attrs={"class": "form-control"}),
        }
