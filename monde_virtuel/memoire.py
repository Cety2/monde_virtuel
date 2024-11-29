from collections import deque

class MemoirePartagee:
    def __init__(self):
        self.memoire = deque()

    def ajouter(self, information):
        self.memoire.append(information)
        print(f"Information ajoutée à la mémoire partagée : {information}")

    def lire(self):
        return list(self.memoire) if self.memoire else []

    def supprimer(self):
        if self.memoire:
            information = self.memoire.popleft()
            print(f"Information supprimée de la mémoire partagée : {information}")
