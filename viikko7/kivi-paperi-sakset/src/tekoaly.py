from toinen_pelaaja import ToinenPelaaja

class Tekoaly(ToinenPelaaja):
    def __init__(self):
        super().__init__()

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"
