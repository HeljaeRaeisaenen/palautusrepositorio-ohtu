from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset_kori = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        määrä = 0

        for nimi in self.ostokset_kori:
            määrä += self.ostokset_kori[nimi].lukumaara()
        
        return määrä

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0

        for nimi in self.ostokset_kori:
            hinta += self.ostokset_kori[nimi].hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() not in self.ostokset_kori:
            ostos = Ostos(lisattava)
            self.ostokset_kori[lisattava.nimi()] = ostos
            return
        self.ostokset_kori[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        nimi = poistettava.nimi()

        if not nimi in self.ostokset_kori:
            return
        
        self.ostokset_kori[nimi].muuta_lukumaaraa(-1)
        if self.ostokset_kori[nimi].lukumaara() == 0:
            self.ostokset_kori.pop(nimi)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostokset_kori = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        return list(self.ostokset_kori.values())
