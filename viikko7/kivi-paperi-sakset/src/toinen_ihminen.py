from toinen_pelaaja import ToinenPelaaja

class ToinenIhminen:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        siirto = input("Toisen pelaajan siirto: ")
        return siirto

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
    
    def valittu_siirto_tieto(self, siirto):
        pass

