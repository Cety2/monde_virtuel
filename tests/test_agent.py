import unittest
from monde_virtuel.agent import Agent, AgentTransaction
from monde_virtuel.memoire import MemoirePartagee

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent("AgentTest")
        self.memoire = MemoirePartagee()

    def test_percevoir_temps(self):
        self.agent.percevoir_temps()
        self.assertTrue(self.agent.energie_physique.niveau > 0)

    def test_ajouter_message_memoire_partagee(self):
        self.agent.ajouter_message_memoire_partagee(self.memoire)
        self.assertIn("Message ajouté par AgentTest", self.memoire.lire())

    def test_loi_gravite(self):
        position_avant = self.agent.position
        self.agent.loi_gravite()
        self.assertNotEqual(position_avant, self.agent.position)

class TestAgentTransaction(unittest.TestCase):
    def setUp(self):
        self.agent_transaction = AgentTransaction("AgentTransactionTest")
        self.memoire = MemoirePartagee()

    def test_gerer_transaction(self):
        self.agent_transaction.gerer_transaction(50, "Mensuel", self.memoire)
        self.assertIn("AgentTransactionTest - Contribution de 50 €", self.memoire.lire())

    def test_verifier_contribution(self):
        self.agent_transaction.gerer_transaction(50, "Mensuel", self.memoire)
        self.assertTrue(self.agent_transaction.verifier_contribution())

if __name__ == '__main__':
    unittest.main()

