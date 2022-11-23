from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset_kori = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        #if len(self.ostokset_kori) == 0: return 0
        määrä = 0
        print(self.ostokset_kori)
        for nimi in self.ostokset_kori:
            määrä += self.ostokset_kori[nimi].lukumaara()
        
        return määrä

    def hinta(self):
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        self.ostokset_kori[lisattava.nimi()] = ostos

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        self.ostokset_kori = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
