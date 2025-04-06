from django.db import models
from django.contrib.auth.models import User
import secrets
import string
from educat.models.groupe_models import Groupe
from BEducat_v1.settings import ROLE_ENSIGNANT

class Enseignant(models.Model):
    user = models.OneToOneField(User,null=True, blank=True ,on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    role = models.CharField(choices=ROLE_ENSIGNANT, max_length=255)
    cin = models.CharField(max_length=255, unique=True)
    photo_profil = models.FileField(upload_to="profil_prof/%Y/%m/%d/", blank=True, null=True)
    groupes = models.ManyToManyField(Groupe, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    @classmethod
    def generate_password(cls, length=8):
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def c_create(self):
        try:
            # Générer le username
            nom = self.nom[:3].lower()  # Prendre les 3 premières lettres du nom
            prenom = self.prenom.lower()  # Prénom en minuscules
            username = f'{nom}.{prenom}'  # Format du username

            # Générer un mot de passe
            password = self.generate_password()

            # Créer un utilisateur
            user = User.objects.create_user(
                username=username,
                password=password
            )

            # Lier l'utilisateur à l'enseignant
            self.user = user
            self.save() 

            return self, f"Prof {self.nom} bien créé. Username: {username}, Password: {password}"

        except Exception as e:
            return None, f"Erreur lors de la création : {str(e)}"

    @classmethod
    def c_list(cls):
        return cls.objects.all()

    def c_update(self):
        try:
            self.save()
            return self, "Enseignant bien mis à jour"
        except Exception as e:
            return None, f"Erreur lors de la mise à jour de l'enseignant : {str(e)}"
