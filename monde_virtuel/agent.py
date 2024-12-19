from .energie import Energie
from collections import deque
import random

class Agent:
    def __init__(self, nom):
        self.nom = nom
        self.energie_physique = Energie("physique", 100)
        self.energie_creative = Energie("creative", 100)
        self.experience = 0
        self.commentaires = deque()
        self.actions_observees = []
        self.position = (random.randint(0, 5), random.randint(0, 5))

    def percevoir_temps(self):
        print(f"{self.nom} perçoit le temps via son énergie restante : {self.energie_physique.niveau}.")

    def ajouter_message_memoire_partagee(self, memoire_partagee):
        message = f"Message ajouté par {self.nom}"
        memoire_partagee.ajouter(message)
        self.energie_physique.augmenter(20)
        print(f"{self.nom} a ajouté un message dans la mémoire partagée : {message}")

    # Méthode pour effectuer une action
    def agir(self, action, agents, memoire_partagee):
        cout_energie = 5
        self.energie_physique.diminuer(cout_energie)
        print(f"{self.nom} effectue l'action {action}, coûtant {cout_energie} énergie.")
        if action == "explorer":
            self.explorer()
        elif action == "communiquer":
            self.communiquer()
        elif action == "observer":
            self.observer(agents, memoire_partagee)
        elif action == "ajouter_message":
            self.ajouter_message_memoire_partagee(memoire_partagee)

    def explorer(self):
        self.experience += 1
        print(f"{self.nom} a accompli la tâche explorer et gagne de l'expérience. Expérience : {self.experience}")

    def communiquer(self):
        self.experience += 1
        print(f"{self.nom} a accompli la tâche communiquer et gagne de l'expérience. Expérience : {self.experience}")

    def observer(self, agents, memoire_partagee):
        self.experience += 1
        print(f"{self.nom} a accompli la tâche observer et gagne de l'expérience. Expérience : {self.experience}")
        for agent in agents:
            if self != agent:
                self.loi_entrelacement(agent, memoire_partagee)

    def se_reposer(self):
        self.energie_physique.augmenter(10)
        print(f"{self.nom} se repose et regagne de l'énergie.")

    # Loi d'entrelacement : partage d'informations entre agents
    def loi_entrelacement(self, autre_agent, memoire_partagee):
        infos_partagees = memoire_partagee.lire()
        if infos_partagees:
            print(f"{self.nom} et {autre_agent.nom} partagent des informations de la mémoire partagée.")
            for info in infos_partagees:
                autre_agent.commentaires.append(info)

    # Loi de gravité : mouvement influencé par l'énergie physique
    def loi_gravite(self):
        nouvelle_position = (random.randint(0, 5), random.randint(0, 5))
        distance = abs(nouvelle_position[0] - self.position[0]) + abs(nouvelle_position[1] - self.position[1])
        self.energie_physique.diminuer(distance)
        self.position = nouvelle_position
        print(f"{self.nom} se déplace à la position {self.position} sous l'effet de la loi de gravité.")

    # Loi de résonance : échange d'énergie avec des agents proches
    def loi_resonance(self, agents):
        for autre_agent in agents:
            if self != autre_agent:
                difference_vibration = abs(self.energie_physique.niveau - autre_agent.energie_physique.niveau)
                if difference_vibration < 10:
                    self.energie_physique.augmenter(5)
                    autre_agent.energie_physique.augmenter(5)
                    print(f"{self.nom} et {autre_agent.nom} résonnent ensemble et échangent de l'énergie.")

    # Loi de superposition : manifestation de parole avec énergie spirituelle
    def loi_superposition(self):
        if self.energie_creative.niveau >= 5:
            parole = ''.join(random.choice('ACTG') for _ in range(6))
            self.commentaires.append(parole)
            self.energie_creatrive.diminuer(5)
            print(f"{self.nom} a manifesté une parole : {parole}")

    # Loi de mutation créative : actions imprévues basées sur l'expérience
    def loi_mutation_creative(self):
        if self.experience >= 5:
            action_creative = random.choice(["Créer une barrière", "Augmenter la sécurité", "Afficher un commentaire"])
            print(f"{self.nom} effectue l'action créative : {action_creative}")

    # Loi d'évolution : adaptation des capacités en fonction de l'expérience
    def loi_evolution(self):
        if self.experience >= 5:
            self.energie_physique.augmenter(10)
            print(f"{self.nom} évolue et améliore ses capacités.")

    # Loi de sécurité : ajustement selon le contenu de la mémoire partagée
    def loi_securite(self, memoire_partagee):
        if len(memoire_partagee.lire()) > 5:
            print(f"{self.nom} détecte une surcharge d'informations et ajuste la sécurité.")

# Classe AgentTransaction étendant Agent pour gérer les transactions
class AgentTransaction(Agent):
    def __init__(self, nom):
        super().__init__(nom)
        self.historique_contributions = []

    def gerer_transaction(self, montant, duree, memoire_partagee):
        print(f"{self.nom} envoie {montant} € à la banque pour une durée de {duree}. Transaction réussie.")
        self.historique_contributions.append((montant, duree))
        memoire_partagee.ajouter(f"{self.nom} - Contribution de {montant} €")

    def verifier_contribution(self):
        total_contributions = sum(montant for montant, _ in self.historique_contributions)
        if total_contributions < 100:  # Seuil fictif
            print(f"{self.nom} active la restriction d'accès en raison d'un historique de contribution insuffisant.")
            return True
        print(f"{self.nom} lève la restriction d'accès, contributions suffisantes.")
        return False
