from django.db import models
from educat.models.groupe_models import Groupe
from django.utils import timezone

class Etudient(models.Model):
    NIVEAUX_LANGUE = [
        ("A1", "A1 - Débutant"),
        ("A2", "A2 - Élémentaire"),
        ("B1", "B1 - Intermédiaire"),
        ("B2", "B2 - Avancé"),
        ("C1", "C1 - Expérimenté"),
        ("C2", "C2 - Maîtrise"),
    ]

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)
    date_inscription = models.DateTimeField(auto_now_add=True)
    photo_profil = models.FileField(upload_to="profil_prof/%Y/%m/%d/", null=True, blank=True)
    niveau = models.CharField(max_length=2, choices=NIVEAUX_LANGUE, default="A1")
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    def c_create(self):
        try:
            self.save() 
            return self, "Etudient bien ajouté"
        except Exception as e:
            return None, f"Erreur lors de l'ajout de l'etudient : {str(e)}"
    @classmethod
    def get_inscription_ce_mois(cls):
        current_month = timezone.now().month
        current_year = timezone.now().year
        return cls.objects.filter(date_inscription__month=current_month, date_inscription__year=current_year).count()
    
    @classmethod
    def get_inscription_total(cls):
        return cls.objects.all().count()
     
