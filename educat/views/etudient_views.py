from django.shortcuts import render ,redirect 
from django.urls import reverse
from educat.models import Etudient
from educat.forms import CreerInscriptionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_etudiant(request):
    if request.method == "POST":
        form = CreerInscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            cin = form.cleaned_data.get('cin')
            photo_profil = form.cleaned_data.get('photo_profil')
            groupe = form.cleaned_data.get('groupe')

            etudient = Etudient(
                nom=nom,
                prenom=prenom,
                cin=cin,
                photo_profil=photo_profil,
                groupe=groupe,
            )

            obj, message = etudient.c_create()
            if obj:
                messages.success(request, message)
                return redirect(reverse('educat:etudiant_list'))
            else:
                messages.error(request, message)

    else:
        form = CreerInscriptionForm()

    context = {
        "form": form
    }
    return render(request, "etudient/etudient_create.html", context)

@login_required
def etudiant(request):
    qset = Etudient.objects.all()
    context = {
        "qset" : qset
    }
    return render(request,"etudient/etudient_list.html",context)
