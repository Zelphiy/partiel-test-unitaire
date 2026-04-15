from src.joueur import Joueur
from src.type_forfait_enum import TypeForfait

def test_creation_joueur():
    joueur = Joueur("Alice", TypeForfait.Forfait)
    assert joueur.nom == "Alice"
    assert joueur.type_forfait == TypeForfait.Forfait