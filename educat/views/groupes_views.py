from django.shortcuts import render ,redirect 
from django.urls import reverse
from educat.models import Groupe ,Etudient
from educat.forms import CreerMatiereForm
from django.contrib import messages

def groupes(request):
    
    qset = Groupe.objects.all()
    context = {
        "qset" : qset,
    }
    return render(request,"groupes/groupes_list.html",context)