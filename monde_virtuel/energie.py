class Energie:
    def __init__(self, type_energie, niveau):
        self.type_energie = type_energie
        self.niveau = niveau

    def augmenter(self, quantite):
        self.niveau += quantite
        print(f"Énergie {self.type_energie} augmentée de {quantite}. Niveau actuel : {self.niveau}")

    def diminuer(self, quantite):
        self.niveau = max(0, self.niveau - quantite)
        print(f"Énergie {self.type_energie} diminuée de {quantite}. Niveau actuel : {self.niveau}")
