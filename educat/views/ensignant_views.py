from django.shortcuts import render , redirect
from django.urls import reverse
from educat.forms.ensignant_forms import CreerEnseignantForm
from educat.models import Enseignant ,Matiere
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def ensignant(request):
    qset = Enseignant.objects.all()
    context = {
        "qset" : qset
    }
    return render(request,"ensignant/ensignant_list.html",context)
@login_required
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
                return redirect(reverse('educat:ensignant_list'))
            else:
                messages.error(request, message)

    else:
        form = CreerEnseignantForm()

    context = {
        "form": form
    }
    return render(request, "ensignant/ensignant_create.html", context)
@login_required
def ensignant_consulter(request,ensignant_id):
    instance = get_object_or_404(Enseignant,pk = ensignant_id)
    list_matiere = Matiere.get_groupes_matiere_enseignant(ensignant_id)
    if request.method == "POST":
        if request.POST.get('action') == "reset_password":
            obj,message = instance.reset_password()
            if obj:
                messages.success(request, message)
                return redirect(reverse('educat:ensignant_list'))
            else:
                messages.error(request, message)
    context = {
        "instance" : instance,
        "list_matiere":list_matiere
    }
    return render(request, "ensignant/ensignant_consulter.html", context)

@login_required
def ensignant_modifier(request, ensignant_id):
    instance = get_object_or_404(Enseignant, pk=ensignant_id)

    if request.method == "POST":
        form = CreerEnseignantForm(request.POST, request.FILES, instance=instance)
        
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            cin = form.cleaned_data['cin']
            role = form.cleaned_data['role']
            photo_profil = form.cleaned_data['photo_profil']
            instance.nom = nom
            instance.prenom = prenom
            instance.cin = cin
            instance.role = role
            instance.photo_profil = photo_profil
            obj, message =instance.c_update()
            if obj:
                messages.success(request, message)
                return redirect(reverse('educat:ensignant_list'))
            else:
                messages.error(request, message)
            context = {
                'form': form,
                'message': "Enseignant bien mis à jour"
            }
            return render(request, 'ensignant/ensignant_modifier.html', context)
    else:
        form = CreerEnseignantForm(instance=instance)

    context = {
        'form': form
    }
    return render(request, 'ensignant/ensignant_modifier.html', context)
     
