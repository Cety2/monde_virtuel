import unittest
from monde_virtuel.agent import Agent, AgentTransaction
from monde_virtuel.memoire import MemoirePartagee
from monde_virtuel.simulation import simuler_cycles

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.agents = [Agent(f"Agent-{i}") for i in range(1, 3)] # Possibilité d'augmenter le nombre d'agents
        self.agent_transaction = AgentTransaction("AgentTransactionTest")
        self.memoire_partagee = MemoirePartagee()

    def test_simuler_cycles(self):
        simuler_cycles(self.agents, self.agent_transaction, self.memoire_partagee, 1) # Augmenter le nombre de cycles
        # Vérifiez si les agents ont exécuté au moins une action
        self.assertTrue(any(agent.experience > 0 for agent in self.agents))

if __name__ == '__main__':
    unittest.main()
