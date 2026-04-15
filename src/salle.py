class Salle:
    def __init__(self, capacite: int, disponibilite: bool, inscrits: list, type_sport):
        self.capacite = capacite
        self.disponibilite = disponibilite
        self.inscrits = inscrits
        self.type_sport = type_sport