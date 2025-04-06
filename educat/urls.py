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
    path("ensignant/<int:ensignant_id>/", views.ensignant_consulter, name="ensignant_consulter"),
    path("ensignant/<int:ensignant_id>/modifier", views.ensignant_modifier, name="ensignant_modifier"),
    ########################################
    ############matiere###################
    #######################################
    path("matiere/",views.matiere,name="matiere_list"),
    path("matiere/créer/",views.create_matiere,name="matiere_create"), 
    ########################################
    ############Groupes###################
    #######################################
    path("groupes/",views.groupes,name="groupes_list"),
    path("groupes/créer/",views.create_groupes,name="groupes_create"),
    path("groupes/<int:groupe_id>/",views.groupe_consulter,name="groupe_consulter"),
     ########################################
    ############Etudient###################
    #######################################
    path("etudiant/",views.etudiant,name="etudiant_list"),
    path("etudiant/créer/",views.create_etudiant,name="etudiant_create"),
    ########################################
    ############auth###################
    #######################################
    path('login/',views.login_view,name="loginE"),
    path('change-password/', views.change_password_view, name='change_password'),
    path('logout/', views.logout_views, name='logout'),

    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
