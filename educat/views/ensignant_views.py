from django.shortcuts import render , redirect
from django.urls import reverse
from educat.forms.ensignant_forms import CreerEnseignantForm
from educat.models import Enseignant
from django.contrib import messages

def ensignant(request):
    qset = Enseignant.objects.all()
    context = {
        "qset" : qset
    }
    return render(request, "ensignant/ensignant_list.html",context)

def create_ensignant(request):
    if request.method == "POST":
        form = CreerEnseignantForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            cin = form.cleaned_data.get('cin')
            role = form.cleaned_data.get('role')
            photo_profil = form.cleaned_data.get('photo_profil')

            prof = Enseignant(
                nom=nom,
                prenom=prenom,
                cin=cin,
                role=role,
                photo_profil=photo_profil
            )

            obj, message = prof.c_create()
            if obj:
                messages.success(request, message)
                return redirect(reverse('ensignant_list'))
            else:
                messages.error(request, message)

    else:
        form = CreerEnseignantForm()

    context = {
        "form": form
    }
    return render(request, "ensignant/ensignant_create.html", context)
