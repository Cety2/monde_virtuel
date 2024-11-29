import unittest
from monde_virtuel.memoire import MemoirePartagee

class TestMemoirePartagee(unittest.TestCase):
    def setUp(self):
        self.memoire = MemoirePartagee()

    def test_ajouter_lire(self):
        self.memoire.ajouter("information 1")
        self.memoire.ajouter("information 2")
        self.assertEqual(self.memoire.lire(), ["information 1", "information 2"])

    def test_supprimer(self):
        self.memoire.ajouter("info 1")
        self.memoire.supprimer()
        self.assertEqual(self.memoire.lire(), [])

if __name__ == '__main__':
    unittest.main()
