from django import forms
from educat.models import Enseignant

class CreerEnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'role', 'cin', 'photo_profil']
        widgets = {
            'nom': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer ton nom...'}),
            'prenom': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer ton prénom...'}),
            'role': forms.Select(attrs={"class": "form-control"}),
            'cin': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer ton CIN...'}),
            'photo_profil': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }

