class CCoinBox:
    monnaie_totale = 0
    monnaie_courante = 0
    vente_permise = False

    def __init__(self):
        self.reset()

    def ajouter_25c(self):
        self.monnaie_courante = self.monnaie_courante + 1
        if self.monnaie_courante >= 1:
            self.vente_permise = True
        print("Une pièce a été ajoutée")

    def vente(self):
        if self.vente_permise:
            self.monnaie_totale = self.monnaie_totale + 2
            self.monnaie_courante = self.monnaie_courante - 2
            print("Vente! Voici votre article ...")
            if self.monnaie_courante < 2:
                self.vente_permise = False
        else:
            print("Pas assez de monnaie")

    def reset(self):
        self.monnaie_totale = 0
        self.monnaie_courante = 0
        self.vente_permise = False
        print("Réinitialisation")

    def retourne_monnaie(self):
        pieces = self.monnaie_courante
        self.monnaie_courante = 0
        self.vente_permise = False
        print("Voici votre monnaie")
        return pieces

    def get_monnaie_totale(self):
        return self.monnaie_totale

    def get_monnaie_courante(self):
        return self.monnaie_courante

    def get_vente_permise(self):
        return self.vente_permise