from src.joueur import Joueur
from src.salle import Salle
from src.reservation import Reservation
from src.type_forfait_enum import TypeForfait
from src.type_sport_enum import TypeSport

def test_creation_reservation():
    joueur = Joueur("Alice", TypeForfait.Forfait)
    salle = Salle(10, True, [], TypeSport.Tennis)
    reservation = Reservation("10:00-11:00", joueur, salle)
    assert reservation.horraires == "10:00-11:00"
    assert reservation.joueur == joueur
    assert reservation.salle == salle