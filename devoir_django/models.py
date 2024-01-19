import datetime
class _item:
    def __init__(self, name):
        self.name = name
        self.disponible = True
        self.dateEmprunt = None
        self.emprunteur = None
    def getName(self):
        return self.name

    def emprunt(self,Emprunteur):
        self.disponible = False
        self.dateEmprunt = datetime.date.today()
        self.emprunteur = Emprunteur.name
    def rendre(self):
        self.disponible = True
        self.dateEmprunt = None
        self.emprunteur = None
class bibliothèque():
    listMédia = []
    listMembre = []
    def __init__(self,name):
        self.name = name

    def ajoutMembre(self,Utilisateur):
        self.listMembre.append(Emprunteur(Utilisateur,self))
        if Utilisateur.bibliothèque is None:
            Utilisateur.bibliothèque = self
    def supprssionMembre(self,Utilisateur):
        self.listMembre.remove(Utilisateur)
        del Utilisateur
        return True
    def changementNomMembre(self,Utilisateur,name):
        print(Utilisateur,name)
        Utilisateur.name.name = name
        return True
    def modificationMembre(self,Utilisateur,bloque):
        Utilisateur.bloque = bloque
    def ajoutMédia(self,_item):
        self.listMédia.append(_item)
        _item.bibliothèque = self
    def supprssionMédia(self,_item):
        self.listMédia.remove(_item)
        _item.bibliothèque = None
    def changementNomMédia(self,_item,name):
        _item.name = name
    def Emprunter(self, _item, Emprunteur):
        if isinstance(_item, jeuDePlateau):
            print(f"Les jeux de plateaux ne sont pas concernés par les emprunts.")
        elif _item in self.listMédia and _item.disponible:
            _item.emprunt(Emprunteur.name)
        else:
            print(f"{_item.name} non trouvé ou indisponible.")

    def rendre(self,_item):
        if _item in self.listMédia and not _item.disponible:
            _item.rendre()


class livre(_item):
    def __init__(self,auteur,name):
        super().__init__(name)
        self.auteur = auteur
class dvd(_item):
    def __init__(self,realisateur,name):
        super().__init__(name)
        self.realisateur = realisateur
class cd(_item):
    def __init__(self,artiste,name):
        super().__init__(name)
        self.artiste = artiste
class jeuDePlateau(_item):
    def __init__(self,createur,name):
        super().__init__(name)
        self.createur = createur

class Utilisateur():
    def __init__(self,name,bibliothèque=None):
        self.bibliothèque=bibliothèque
        self.name = name
class Emprunteur(Utilisateur):
    listEmprunteur = []

    def __init__(self, name, bibliothèque=None):
        super().__init__(name, bibliothèque)
        self.bloque = False

    def Emprunter(self, _item):
        if self.bibliothèque is not None:
            if not self.bloque:
                if len(self.listEmprunteur) < 3:
                    if isinstance(_item, jeuDePlateau):
                        print(f"Les jeux de plateaux ne sont pas concernés par les emprunts.")
                        return False
                    elif _item.disponible:
                        self.bibliothèque.Emprunter(_item,self)
                        self.listEmprunteur.append(_item)
                        return True
                    else:
                        print(f"{_item.name} est indisponible.")
                        return False
                else:
                    print("Erreur : Vous avez déjà emprunté le nombre maximum d'articles (3).")
                    return False
            else:
                print("Erreur : Vous êtes bloqué en raison d'un emprunt en retard.")
                return False
        else:
            print("Erreur")
            return False

    def rendre(self,_item):
        if _item.dateEmprunt:
            today = datetime.date.today()
            delta = today - _item.dateEmprunt
            if delta.days > 7:
                self.emprunteur.bloque = True
        if self.bibliothèque:
            self.bibliothèque.rendre(_item)
            return True




