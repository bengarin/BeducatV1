from django.shortcuts import render
from educat.models import Enseignant ,Etudient
# Create your views here.

def home(request) :
    inscription_ce_mois = Etudient.get_inscription_ce_mois()
    inscription_total = Etudient.get_inscription_total()
    context = {
        "inscription_ce_mois": inscription_ce_mois,
        "inscription_total" :inscription_total,
    }
    return render(request,"index.html",context)
