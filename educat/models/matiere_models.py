from django.db import models
from educat.models.prof_models import Enseignant

class Matiere(models.Model):
    NIVEAUX_LANGUE = [
        ("A1", "A1 - Débutant"),
        ("A2", "A2 - Élémentaire"),
        ("B1", "B1 - Intermédiaire"),
        ("B2", "B2 - Avancé"),
        ("C1", "C1 - Expérimenté"),
        ("C2", "C2 - Maîtrise"),
    ]

    title = models.CharField(max_length=255) 
    code = models.CharField(max_length=15, unique=True) 
    niveau = models.CharField(max_length=2, choices=NIVEAUX_LANGUE)  
    volume_horaire = models.IntegerField(help_text="Volume horaire total en heures")  
    enseignant = models.ForeignKey(Enseignant, blank=True, null=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return f"{self.title} ({self.niveau})"
