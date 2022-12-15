from toinen_pelaaja import ToinenPelaaja

class ToinenIhminen(ToinenPelaaja):
    def __init__(self):
        super().__init__()

    def anna_siirto(self):
        siirto = input("Toisen pelaajan siirto: ")
        return siirto

    def valittu_siirto_tieto(self, siirto):
        pass
