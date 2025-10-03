import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_pass(self):
        pass

    def test_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_retourne_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        piece = coinBox.retourne_monnaie()
        self.assertEqual(coinBox.get_vente_permise(), False)
        self.assertEqual(piece, 1)

    def test_permet_une_double_vente(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.vente()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_reset(self):
        coinBox = CCoinBox()
        coinBox.reset()
        self.assertEqual(coinBox.get_vente_permise(), False)
        self.assertEqual(coinBox.get_monnaie_courante(), 0)
        self.assertEqual(coinBox.get_monnaie_totale(), 0)

