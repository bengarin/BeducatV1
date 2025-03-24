from django import forms
from educat.models import Etudient,Groupe

class CreerInscriptionForm(forms.ModelForm):
    groupe = forms.ModelChoiceField(
        queryset=Groupe.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Sélectionner un groupe"
    )

    class Meta:
        model = Etudient
        fields = ['nom', 'prenom', 'cin', 'photo_profil', 'groupe']
        widgets = {
            'nom': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer ton nom...'}),
            'prenom': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer ton prénom...'}),
            'cin': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Entrer ton CIN...'}),
            'photo_profil': forms.FileInput(attrs={"class": "form-control"}),
        }
