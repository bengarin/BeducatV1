from django.shortcuts import render ,redirect 
from django.urls import reverse
from educat.models import Groupe ,Etudient
from educat.forms import CreerGroupestForm
from django.forms import formset_factory
from django.contrib import messages

def groupes(request):
    
    qset = Groupe.objects.all()
    context = {
        "qset" : qset,
    }
    return render(request,"groupes/groupes_list.html",context)

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
                return redirect(reverse('groupes_list'))
            else:
                messages.error(request, message)

    else:
        form = CreerGroupestForm()
        
    context = {
        "form" : form
    }
    return render(request,"groupes/groupes_create.html",context)
    