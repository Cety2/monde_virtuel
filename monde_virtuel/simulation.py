import time
import random
from collections import deque
from monde_virtuel import Agent, AgentTransaction, MemoirePartagee  # Assurez-vous que Simulation est bien dans monde_virtuel si vous l'y avez ajoutée

class Simulation:
    def __init__(self, agents, agent_transaction, memoire_partagee, nombre_cycles):
        self.agents = agents
        self.agent_transaction = agent_transaction
        self.memoire_partagee = memoire_partagee
        self.nombre_cycles = nombre_cycles
        self.perturbations = deque()  # Utilisation de deque pour les perturbations

    def ajouter_perturbation(self, perturbation):
        """Ajoute une perturbation à la file des perturbations."""
        self.perturbations.append(perturbation)

    def appliquer_perturbations(self):
        """Applique toutes les perturbations définies aux agents."""
        while self.perturbations:
            perturbation = self.perturbations.popleft()  # Récupérer et supprimer la première perturbation
            perturbation(self.agents)

    def lancer(self):
        """Lance la simulation en appliquant les cycles et les perturbations."""
        for cycle in range(self.nombre_cycles):
            print(f"\n--- Cycle {cycle + 1} ---")

            # Appliquer les perturbations tous les 4 cycles (modifiable)
            if cycle % 4 == 0:
                self.appliquer_perturbations()

            # Transaction tous les 3 cycles
            if cycle % 3 == 0:
                montant = random.randint(20, 100)
                duree = random.choice(["Mensuel", "Trimestriel", "Annuel", "Unique"])
                self.agent_transaction.gerer_transaction(montant, duree, self.memoire_partagee)

            # Vérifier et gérer l'accès selon l'historique des contributions
            if self.agent_transaction.verifier_contribution():
                print(f"{self.agent_transaction.nom} restreint l'accès à certaines fonctionnalités.")
            else:
                print(f"{self.agent_transaction.nom} permet l'accès complet aux fonctionnalités.")

            # Agents agissent
            for agent in self.agents:
                agent.percevoir_temps()
                agent.ajouter_message_memoire_partagee(self.memoire_partagee)
                agent.loi_gravite()
                agent.loi_resonance(self.agents)
                agent.loi_superposition()
                agent.loi_mutation_creative()
                agent.loi_evolution()
                agent.loi_securite(self.memoire_partagee)
                action = random.choice(["explorer", "communiquer", "observer", "ajouter_message"])
                agent.agir(action, self.agents, self.memoire_partagee)
                agent.se_reposer()

            # Nettoyage de la mémoire tous les 5 cycles
            if cycle % 5 == 0:
                self.memoire_partagee.supprimer()

            # Pause entre les cycles (pour un délai minimal ici)
            time.sleep(0)

# Exemple d'implémentation d'une perturbation
def perturber_gravite(agents):
    """Exemple de perturbation qui modifie temporairement la gravité."""
    print("\n!!! Perturbation de gravité !!!")
    for agent in agents:
        agent.energie_physique.diminuer(random.randint(5, 15))
        print(f"{agent.nom} subit une perturbation de gravité et perd de l'énergie.")

def reduction_energie(agents):
    """Exemple de perturbation qui réduit l'énergie de chaque agent."""
    print("\n!!! Perturbation de réduction d'énergie !!!")
    for agent in agents:
        agent.energie_physique.diminuer(random.randint(10, 20))
        print(f"{agent.nom} perd de l'énergie à cause d'une perturbation d'énergie.")

# Initialisation de la simulation
agents = [Agent(nom=f"Agent-{i}") for i in range(5)]  # Créez un nombre d'agents automatiquement
agent_transaction = AgentTransaction(nom="TransactionAgent")
memoire_partagee = MemoirePartagee()
simulation = Simulation(agents, agent_transaction, memoire_partagee, nombre_cycles=20)

# Ajout des perturbations pour le test dans Colab
simulation.ajouter_perturbation(perturber_gravite)
simulation.ajouter_perturbation(reduction_energie)

# Lancer la simulation
simulation.lancer()

