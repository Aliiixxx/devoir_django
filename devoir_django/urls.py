"""
URL configuration for devoir_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('emprunteurs/', views.index_emprunteur, name='index_emprunteur'),
    path('emprunteurs/emprunter/', views.emprunter_media, name='emprunter_media'),
    path('emprunteurs/rendre/', views.rendre_media, name='rendre_media'),

    path('bibliothecaires/', views.index_bibliothecaire, name='index_bibliothecaire'),
    path('bibliothecaires/ajouter_membre/', views.ajouter_membre, name='ajouter_membre'),
    path('bibliothecaires/modifier_membre/', views.modifier_membre, name='modifier_membre'),
    path('bibliothecaires/afficher_membres/', views.afficher_membres, name='afficher_membres'),
    path('bibliothecaires/creer_emprunt/', views.creer_emprunt, name='creer_emprunt'),
    path('bibliothecaires/ajouter_media/', views.ajouter_media, name='ajouter_media'),
    path('bibliothecaires/rentrer_emprunt/', views.rentrer_emprunt, name='rentrer_emprunt'),
    path('supprimer_membre/', views.supprimer_membre, name='supprimer_membre'),
    path('', views.accueil, name='accueil')
]
