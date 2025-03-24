from django.db import models

class Groupe (models.Model) :
    name= models.CharField(max_length=30,unique=True)
    description = models.TextField(null=True,blank=True)
    max_inscription = models.IntegerField(max_length=255,default=0)
    
    def __str__(self):
        return self.name
    
    def count_inscription(self):
        from educat.models.etudient_models import Etudient
        return Etudient.objects.filter(groupe = self).count()
    
    
    def c_create(self):
        try:
            self.save() 
            return self, "Enseignant bien ajouté"
        except Exception as e:
            return None, f"Erreur lors de l'ajout de l'enseignant : {str(e)}"
