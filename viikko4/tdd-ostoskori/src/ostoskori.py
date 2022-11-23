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
        hinta = 0

        for nimi in self.ostokset_kori:
            hinta += self.ostokset_kori[nimi].hinta()

        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() not in self.ostokset_kori:
            ostos = Ostos(lisattava)
            self.ostokset_kori[lisattava.nimi()] = ostos
            return
        self.ostokset_kori[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        self.ostokset_kori = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.ostokset_kori.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
