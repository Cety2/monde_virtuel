import unittest
from monde_virtuel.energie import Energie

class TestEnergie(unittest.TestCase):
    def setUp(self):
        self.energie = Energie("physique", 100)

    def test_augmenter(self):
        self.energie.augmenter(20)
        self.assertEqual(self.energie.niveau, 120)

    def test_diminuer(self):
        self.energie.diminuer(50)
        self.assertEqual(self.energie.niveau, 50)

    def test_diminuer_below_zero(self):
        self.energie.diminuer(200)
        self.assertEqual(self.energie.niveau, 0)

if __name__ == '__main__':
    unittest.main()
