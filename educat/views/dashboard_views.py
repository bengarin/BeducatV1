from django.shortcuts import render
from educat.models import Enseignant ,Etudient
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def home(request) :
    inscription_ce_mois = Etudient.get_inscription_ce_mois()
    inscription_total = Etudient.get_inscription_total()
    instance = get_object_or_404(Enseignant,user = request.user)
    print(instance)
    context = {
        "instance":instance,
        "inscription_ce_mois": inscription_ce_mois,
        "inscription_total" :inscription_total,
    }
    return render(request,"index.html",context)
