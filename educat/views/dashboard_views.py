from django.shortcuts import render
from educat.models import Enseignant
# Create your views here.

def home(request) :
    print(Enseignant.c_list())
    return render(request,"index.html")
