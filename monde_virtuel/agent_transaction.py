# agent_transaction.py
# sysstème adapté pour les aboonements flexible

from .agent import Agent
from .memoire import MemoirePartagee

class AgentTransaction(Agent):
    def __init__(self, name):
        super().__init__(name, user_id=None)
        self.historique_contributions = []

    def gerer_transaction(self, montant, duree, memoire_partagee):
        print(f"{self.name} envoie {montant} € pour une durée de {duree}. Transaction réussie.")
        self.historique_contributions.append((montant, duree))
        memoire_partagee.ajouter(f"{self.name} - Contribution de {montant} €")

    def verifier_contribution(self):
        total_contributions = sum(montant for montant, _ in self.historique_contributions)
        if total_contributions < 100:
            print(f"{self.name} active la restriction d'accès en raison d'un historique de contribution insuffisant.")
            return True
        print(f"{self.name} lève la restriction d'accès, contributions suffisantes.")
        return False
