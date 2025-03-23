from django.contrib import admin
from .models import Enseignant , Matiere , Groupe ,Etudient

# Register your models here.
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Groupe)
admin.site.register(Etudient)
