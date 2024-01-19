from django.shortcuts import render
from manage import bibliotheque
from .models import Utilisateur
from django.shortcuts import redirect
from .models import livre, dvd, cd, jeuDePlateau
from django.http import HttpResponse


def menuBibliotheque():
    print("c'est le menu de l'application des bibliothéquaire")


def menuMembre():
    print("c'est le menu de l'application des membres")
    print("affiche tout")


def printListeMembre(bibliotheque):
    [print(vars(obj)) for obj in bibliotheque.listMembre]


def printListeMedia(bibliotheque):
    [print(vars(obj)) for obj in bibliotheque.listMédia]


def index_emprunteur(request,user_name):
    medias_disponibles = bibliotheque.listMédia
    liste_utilisateurs = bibliotheque.listMembre
    for media in medias_disponibles:
        media.class_name = media.__class__.__name__

    context = {
        'medias_disponibles': medias_disponibles,
        'liste_utilisateurs': liste_utilisateurs,
        'user_name': user_name

    }
    return render(request, 'index_emprunteur.html', context)


def emprunter_media(request):
    media_name = request.GET.get('media_name', '')
    user_name = request.GET.get('user_name', '')
    if (request.GET.get('mybtn')):
        media = next((m for m in bibliotheque.listMédia if m.name == request.GET.get('mytextbox')), None)
        if media:
            user = next((m for m in bibliotheque.listMembre if m.name.name == user_name), None)
            if user:
                emprunt_result = user.Emprunter(media)
                return render(request, 'emprunter_media.html', {'emprunt_result': emprunt_result, 'media_name': media_name})
    return render(request, 'emprunter_media.html', {'media_name': media_name})


def rendre_media(request):
    media_name = request.GET.get('media_name', '')
    user_name = request.GET.get('user_name', '')
    if (request.GET.get('mybtn')):
        media = next((m for m in bibliotheque.listMédia if m.name ==request.GET.get('mytextbox')), None)
        if media:
            print(media.emprunteur,user_name)
            if media.emprunteur == user_name:
                user = next((m for m in bibliotheque.listMembre if m.name.name == user_name), None)
                print(user)
                if user :
                    print('slt',user.name)
                    rendre_result = user.rendre(media)
                    return render(request, 'rendre_media.html', {'emprunt_result': rendre_result, 'media_name': media_name})
        else:
            return render(request, 'rendre_media.html', {'emprunt_result': False, 'media_name': media_name})
    return render(request, 'rendre_media.html', {'media_name': media_name})


def index_bibliothecaire(request):
    medias_disponibles = bibliotheque.listMédia
    liste_utilisateurs = bibliotheque.listMembre
    for utilisateur in liste_utilisateurs:
        print(utilisateur.bibliothèque.name)
        utilisateur.name.listmedia = []
    for media in medias_disponibles:
        media.class_name = media.__class__.__name__
        if isinstance(media,livre):
            media.infos_supp=media.auteur
        elif isinstance(media,dvd):
            media.infos_supp=media.realisateur
        elif isinstance(media,cd):
            media.infos_supp=media.artiste
        elif isinstance(media,jeuDePlateau):
            media.infos_supp=media.createur
    for media in medias_disponibles:
        if media.disponible is False :
            for utilisateur in liste_utilisateurs:
                if media.emprunteur ==utilisateur.name.name:
                    utilisateur.name.listmedia.append(media.name)

    context = {
        'medias_disponibles': medias_disponibles,
        'liste_utilisateurs': liste_utilisateurs,

    }
    return render(request, 'index_bibliothecaire.html',context)


def ajouter_membre(request):
    message = ""

    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom_utilisateur')
        if nom_utilisateur:
            nouvel_utilisateur = Utilisateur(nom_utilisateur)
            bibliotheque.ajoutMembre(nouvel_utilisateur)
            message = "Utilisateur ajouté avec succès!"

    return render(request, 'ajouter_membre.html', {'message': message})


def modifier_membre(request):
    membre_name = request.GET.get('membre_name')
    if (request.GET.get('mybtn')):
        user = next((m for m in bibliotheque.listMembre if m.name.name == membre_name), None)
        if user:
            modifier_result = bibliotheque.changementNomMembre(user,request.GET.get('newName'))
            return render(request, 'modifier_membre.html', {'modifier_result': modifier_result, 'membre_name': membre_name})
    return render(request, 'modifier_membre.html',{'membre_name': membre_name})


def afficher_membres(request):
    return render(request, 'afficher_membres.html')


def afficher_medias(request):
    return render(request, 'afficher_medias.html')


def creer_emprunt(request):
    return render(request, 'creer_emprunt.html')


def ajouter_media(request):
    message = ""


    if request.method == 'POST':
        nom_media = request.POST.get('nom_media')
        type_media = request.POST.get('type_media')
        infos_createur = request.POST.get('infos_createur')
        media = next((m for m in bibliotheque.listMédia if m.name == request.GET.get('mytextbox')), None)
        if not media :
            if nom_media and type_media:
                if type_media == "livre":
                    nouveau_media = livre(infos_createur,nom_media)
                elif type_media == "dvd":
                    nouveau_media = dvd(infos_createur,nom_media)
                elif type_media == "cd":
                    nouveau_media = cd(infos_createur,nom_media)
                elif type_media == "jeu_de_plateau":
                    nouveau_media = jeuDePlateau(infos_createur,nom_media)
                else:
                    return HttpResponse("Type de média non valide!")

                bibliotheque.ajoutMédia(nouveau_media)
                message = "Média ajouté avec succès!"
        else:
            message='Média déja éxistant'
    medias_disponibles = bibliotheque.listMédia

    return render(request, 'ajouter_media.html', {'message': message, 'medias_disponibles': medias_disponibles})


def rentrer_emprunt(request):
    return render(request, 'rentrer_emprunt.html')


def supprimer_membre(request):
    if request.method == 'POST':
        membre_name = request.POST.get('membre_name')
        user = next((m for m in bibliotheque.listMembre if m.name.name == membre_name), None)
        if user:
            result_delete=bibliotheque.supprssionMembre(user)
        else:
            result_delete=False
    return redirect('/bibliothecaires/')

def accueil(request):
    if request.method == 'POST':
        membre_name = request.POST.get('membre_name')
        user = next((m for m in bibliotheque.listMembre if m.name.name == membre_name), None)
        if user:
            return index_emprunteur(request,membre_name)
        else:
            return render(request, 'accueil.html',{'user_exist':True})
    return render(request, 'accueil.html')



