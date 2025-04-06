from django.db import models
from django.contrib.auth.models import User
import secrets
import string
from educat.models.groupe_models import Groupe
from BEducat_v1.settings import ROLE_ENSIGNANT

class Enseignant(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    role = models.CharField(choices=ROLE_ENSIGNANT, max_length=255)
    cin = models.CharField(max_length=255, unique=True)
    photo_profil = models.FileField(upload_to="profil_prof/%Y/%m/%d/", blank=True, null=True)
    groupes = models.ManyToManyField(Groupe, blank=True)
    is_first_login = models.BooleanField(default=True)
    temp_password = models.CharField(max_length=255, blank=True, null=True)  # Mot de passe temporaire
    def __str__(self):
        return f"{self.nom} {self.prenom}"

    @classmethod
    def generate_password(cls, length=8):
        """ Génère un mot de passe temporaire. """
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def c_create(self):
        try:
            nom = self.nom[:3].lower() 
            prenom = self.prenom.lower() 
            username = f'{nom}.{prenom}' 
            password = self.generate_password()

            user = User.objects.create_user(
                username=username,
                password=password
            )

            self.user = user
            self.temp_password = password 
            self.save()

            return self, f"Prof {self.nom} bien créé. Username: {username}, Password: {password}"

        except Exception as e:
            return None, f"Erreur lors de la création : {str(e)}"

    @classmethod
    def c_list(cls):
        """ Liste tous les enseignants """
        return cls.objects.all()

    def c_update(self):
        """ Met à jour les informations d'un enseignant """
        try:
            self.save()
            return self, "Enseignant bien mis à jour"
        except Exception as e:
            return None, f"Erreur lors de la mise à jour de l'enseignant : {str(e)}"

    def update_first_login_status(self):
        """ Met à jour l'état de 'is_first_login' après que l'enseignant ait changé son mot de passe """
        self.is_first_login = False
        self.save()
        
    def reset_password(self):
        try:
            temp_password = self.generate_password()

            self.user.set_password(temp_password)
            self.user.save()
            self.temp_password = temp_password
            self.is_first_login = True
            self.save()

            return True, f"Le mot de passe a été réinitialisé avec succès. Nouveau mot de passe temporaire: {temp_password}"
        
        except Exception as e:
            return False, f"Erreur lors de la réinitialisation du mot de passe: {str(e)}"