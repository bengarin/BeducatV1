from django.db import models
from educat.models.groupe_models import Groupe

class Etudient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)
    date_inscription = models.DateTimeField(auto_now_add=True)
    photo_profil = models.FileField(upload_to="profil_prof/%Y/%m/%d/",null=True ,blank=True)
    groupe = models.ForeignKey(Groupe , on_delete=models.CASCADE , default="") 
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"