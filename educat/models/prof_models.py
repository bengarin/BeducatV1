from django.db import models
from BEducat_v1.settings import ROLE_ENSIGNANT

class Enseignant(models.Model) :
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    role = models.CharField(choices=ROLE_ENSIGNANT ,max_length=255)
    cin = models.CharField(max_length=255, unique=True)
    photo_profil = models.FileField(upload_to="profil_prof/%Y/%m/%d/")
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    @classmethod
    def c_list(cls) :
        return cls.objects.all()
    
    def c_create(self):
        try:
            self.save() 
            return self, "Enseignant bien ajouté"
        except Exception as e:
            return None, f"Erreur lors de l'ajout de l'enseignant : {str(e)}"
