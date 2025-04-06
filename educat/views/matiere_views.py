from django.shortcuts import render ,redirect 
from django.urls import reverse
from educat.models import Matiere
from educat.forms import CreerMatiereForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def matiere(request):
    qset = Matiere.objects.all()
    context= {
        "qset":qset,
    }
    return render(request , "matiere/matiere_list.html",context)

@login_required
def create_matiere(request):
    if request.method == "POST":
        form = CreerMatiereForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            code = form.cleaned_data.get('code')
            niveau = form.cleaned_data.get('niveau')
            volume_horaire = form.cleaned_data.get('volume_horaire')
            enseignant = form.cleaned_data.get('enseignant')

            matiere = Matiere(
                title=title,
                code=code,
                niveau=niveau,
                volume_horaire=volume_horaire,
                enseignant=enseignant
            )

            obj, message = matiere.c_create()
            if obj:
                messages.success(request, message)
                return redirect(reverse('educat:matiere_list'))
            else:
                messages.error(request, message)

    else:
        form = CreerMatiereForm()

    context = {
        "form": form
    }
    return render(request, "matiere/matiere_create.html", context)