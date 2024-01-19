from models import *
from unittest.mock import patch
import datetime



bibliotheque1 = bibliothèque("Bibliothèque principale")

membre1 = Utilisateur("Alice")
membre2 = Utilisateur("Bob")

bibliotheque1.ajoutMembre(membre1)
bibliotheque1.ajoutMembre(membre2)

assert membre1.bibliothèque == bibliotheque1
assert membre2.bibliothèque == bibliotheque1

livre1 = livre("Auteur 1", "Livre 1")
cd1 = cd("Artiste 1", "CD 1")
cd2 = cd("Artiste 2", "CD 2")
cd3 = cd("Artiste 3", "CD 3")
cd4 = cd("Artiste 4", "CD 4")

bibliotheque1.ajoutMédia(livre1)
bibliotheque1.ajoutMédia(cd1)

assert livre1 in bibliotheque1.listMédia
assert cd1 in bibliotheque1.listMédia

emprunteur1 = Emprunteur("Charlie", bibliotheque1)
emprunteur1.name = emprunteur1

result = emprunteur1.Emprunter(livre1)
assert result == True

result = emprunteur1.Emprunter(livre1)
assert result == False

emprunteur1.rendre(livre1)

assert livre1.disponible == True

livre2 = livre("Auteur 2", "Livre 2")
emprunteur1.Emprunter(livre2)
emprunteur1.Emprunter(cd2)
emprunteur1.Emprunter(cd4)
emprunteur1.Emprunter(cd3)
emprunteur1.Emprunter(cd1)
assert cd1.disponible == True
with patch('datetime.datetime') as mock_datetime:
    mock_datetime.today.return_value = datetime.datetime.now() - datetime.timedelta(days=8)
    emprunteur1.rendre(cd3)
assert emprunteur1.rendre(cd2) == True

assert membre1 not in bibliotheque1.listMembre
