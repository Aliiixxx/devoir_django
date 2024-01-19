#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from devoir_django.models import *
from devoir_django.views import *

bibliotheque = bibliothèque('BFM')


def main():
    bibliotheque.ajoutMembre(Emprunteur('nico',bibliotheque))
    bibliotheque.ajoutMembre(Emprunteur('issam',bibliotheque))
    bibliotheque.ajoutMédia(cd('artiste 1' ,'cd 1'))
    bibliotheque.ajoutMédia(dvd('realisateur 1' ,'dvd 1'))
    bibliotheque.ajoutMédia(jeuDePlateau('createur 1','jeu 1'))
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devoir_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def menu():
    bibliotheque = bibliothèque()
    while True:
        print("\nBienvenue dans l'application bibliothécaire.")
        role = input("Êtes-vous un emprunteur (E) ou un bibliothéquaire (B) ? ").lower()

        if role == 'e':
            nom_emprunteur = input("Entrez votre nom d'emprunteur : ")
            emprunteur = next((e for e in bibliotheque.listMembre if e.name == nom_emprunteur), None)

            if emprunteur is None:
                print("Emprunteur non trouvé.")
                continue

            while True:
                print("\nActions disponibles pour l'emprunteur:")
                print("1. Afficher la liste des médias")
                print("2. Emprunter un média")
                print("3. Rendre un emprunt")
                print("4. Quitter")

                choix = input("Choisissez une action (1-4) : ")

                if choix == '1':
                    printListeMedia(bibliotheque)
                elif choix == '2':
                    nom_media = input("Entrez le nom du média que vous souhaitez emprunter : ")
                    media = next((m for m in bibliotheque.listMédia if m.name == nom_media), None)

                    if media:
                        if not isinstance(media, jeuDePlateau):
                            if len(emprunteur.listEmprunteur) < 3:
                                if media.disponible:
                                    emprunteur.Emprunter(media)
                                    print(f"Emprunt de {nom_media} réalisé avec succès.")
                                else:
                                    print(f"{nom_media} est indisponible.")
                            else:
                                print("Vous avez déjà emprunté le nombre maximum d'articles (3).")
                        else:
                            print(f"Les jeux de plateaux ne peuvent pas être empruntés.")
                    else:
                        print(f"{nom_media} non trouvé.")
                elif choix == '3':
                    nom_media = input("Entrez le nom du média que vous souhaitez rendre : ")
                    media = next((m for m in bibliotheque.listMédia if m.name == nom_media), None)

                    if media and not media.disponible and media.emprunteur == emprunteur.name:
                        emprunteur.rendre(media)
                        print(f"Rentrée de l'emprunt de {nom_media} réalisée avec succès.")
                    else:
                        print(f"{nom_media} non trouvé, indisponible ou emprunté par un autre utilisateur.")
                elif choix == '4':
                    print("Merci d'avoir utilisé l'application bibliothécaire. Au revoir!")
                    break
                else:
                    print("Choix non valide. Veuillez choisir une action de 1 à 4.")
        elif role == 'b':
            while True :
                print("\nActions disponibles pour le bibliothéquaire:")
                print("1. Ajouter un membre")
                print("2. Afficher la liste des membres")
                print("3. Mettre à jour un membre")
                print("4. Afficher la liste des médias")
                print("5. Créer un emprunt pour un média disponible")
                print("6. Ajouter un média")
                print("7. Rentrer un emprunt")
                print("8. Quitter")

                choix = input("Choisissez une action (1-7) : ")
                if choix == '1':
                    nom_utilisateur = input("Entrez le nom du membre : ")
                    bibliotheque.ajoutMembre(nom_utilisateur)
                    print(f" {nom_utilisateur} ajouté avec succès.")
                if choix == '2':
                    printListeMembre(bibliotheque)
                elif choix == '3':
                    nom_membre = input("Entrez le nom du membre que vous souhaitez mettre à jour : ")
                    nouveau_nom = input("Entrez le nouveau nom : ")
                    membre = next((m for m in bibliotheque.listMembre if m.name == nom_membre), None)

                    if membre:
                        bibliotheque.changementNomMembre(membre, nouveau_nom)
                        print(f"Nom du membre {nom_membre} mis à jour avec succès.")
                    else:
                        print(f"{nom_membre} non trouvé.")
                elif choix == '4':
                    printListeMedia(bibliotheque)
                elif choix == '5':
                    nom_media = input("Entrez le nom du média que vous souhaitez emprunter : ")
                    nom_emprunteur = input("Entrez le nom de l'emprunteur : ")
                    media = next((m for m in bibliotheque.listMédia if m.name == nom_media), None)
                    emprunteur = next((e for e in Emprunteur.listEmprunteur if e.name == nom_emprunteur), None)

                    if media and media.disponible and emprunteur:
                        emprunteur.Emprunter(media)
                        print(f"Emprunt de {nom_media} par {nom_emprunteur} réalisé avec succès.")
                    else:
                        print(f"{nom_media} non trouvé, indisponible ou emprunteur non trouvé.")
                elif choix == '6':
                    type_media = input("Entrez le type de média (livre, dvd, cd, jeu) : ")
                    nom_media = input("Entrez le nom du média : ")

                    if type_media in ["livre", "dvd", "cd", "jeu"]:
                        if type_media == "livre":
                            nouveau_media = livre("Auteur Inconnu", nom_media)
                        elif type_media == "dvd":
                            nouveau_media = dvd("Réalisateur Inconnu", nom_media)
                        elif type_media == "cd":
                            nouveau_media = cd("Artiste Inconnu", nom_media)
                        elif type_media == "jeu":
                            nouveau_media = jeuDePlateau("Créateur Inconnu", nom_media)

                        bibliotheque.ajoutMédia(nouveau_media)
                        print(f"{type_media.capitalize()} {nom_media} ajouté avec succès.")
                    else:
                        print("Type de média non pris en charge.")
                elif choix == '7':
                    nom_media = input("Entrez le nom du média que vous souhaitez rendre : ")
                    nom_emprunteur = input("Entrez le nom de l'emprunteur : ")
                    media = next((m for m in bibliotheque.listMédia if m.name == nom_media), None)
                    emprunteur = next((e for e in Emprunteur.listEmprunteur if e.name == nom_emprunteur), None)

                    if media and not media.disponible and media.emprunteur == nom_emprunteur:
                        emprunteur.rendre(media)
                        print(f"Rentrée de l'emprunt de {nom_media} par {nom_emprunteur} réalisée avec succès.")
                    else:
                        print(f"{nom_media} non trouvé, indisponible ou emprunteur non trouvé.")
                elif choix == '8': \
                    print("Merci d'avoir utilisé l'application bibliothécaire. Au revoir!")
                break
        else:
            print("Choix non valide. Veuillez choisir une action de 1 à 7.")
    else:
        print("Rôle non valide. Veuillez choisir 'E' pour emprunteur ou 'B' pour bibliothéquaire.")

if __name__ == '__main__':
    main()

