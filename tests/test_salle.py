from src.salle import Salle
from src.type_sport_enum import TypeSport

# Test unitaire pour la classe Salle
def test_creation_salle():
    salle = Salle(10, True, [], TypeSport.Tennis)
    assert salle.capacite == 10
    assert salle.disponibilite == True
    assert salle.inscrits == []
    assert salle.type_sport == TypeSport.Tennis