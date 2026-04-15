from src.joueur import Joueur
from src.salle import Salle

class Reservation:
    def __init__(self, horraires: str, joueur: Joueur, salle: Salle):
        self.horraires = horraires
        self.joueur = joueur
        self.salle = salle
        
    