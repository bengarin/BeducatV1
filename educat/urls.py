from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'educat'
urlpatterns = [
    path('',views.home,name="home"),
    ########################################
    ############ensignant###################
    #######################################
    path("ensignant/",views.ensignant,name="ensignant_list"),
    path("ensignant/créer/",views.create_ensignant,name="ensignant_create"),
    ########################################
    ############matiere###################
    #######################################
    path("matiere/",views.matiere,name="matiere_list"),
    path("matiere/créer/",views.create_matiere,name="matiere_create"), 
    ########################################
    ############Groupes###################
    #######################################
    path("groupes/",views.groupes,name="groupes_list"),
    path("matiere/créer/",views.create_matiere,name="matiere_create"),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
