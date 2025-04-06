from django.shortcuts import render ,redirect 
from django.urls import reverse
from educat.models import Groupe ,Etudient
from educat.forms import CreerGroupestForm
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def groupes(request):
    
    qset = Groupe.objects.all()
    context = {
        "qset" : qset,
    }
    return render(request,"groupes/groupes_list.html",context)
@login_required
def create_groupes(request):
    if request.method == "POST":
        form = CreerGroupestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            max_inscription = form.cleaned_data.get('max_inscription')
            groupe = Groupe(
                name=name,
                description=description,
                max_inscription=max_inscription,
            )

            obj, message = groupe.c_create()
            if obj:
                messages.success(request, message)
                return redirect(reverse('educat:groupes_list'))
            else:
                messages.error(request, message)

    else:
        form = CreerGroupestForm()
        
    context = {
        "form" : form
    }
    return render(request,"groupes/groupes_create.html",context)

def groupe_consulter(request,groupe_id):
    instance = get_object_or_404(Groupe,pk = groupe_id)
    context = {
        "instance" : instance
    }
    return render(request,"groupes/groupe_consulter.html",context)
    