class Sovelluslogiikka:
    def __init__(self, tulos=0, edellinen=0):
        self.tulos = tulos
        self.edellinen_arvo = edellinen

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen_arvo = self.tulos
        self.tulos = arvo


class Summa:
    def __init__(self, logiikka, lue_syote) -> None:
        self.sovelluslogiikka = logiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
            if len(luku) == 0:
                return
        except Exception:
            pass
        
        tulos = self.sovelluslogiikka.tulos + int(luku)
        self.sovelluslogiikka.aseta_arvo(tulos)

class Erotus:
    def __init__(self, logiikka, lue_syote) -> None:
        self.sovelluslogiikka = logiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
            if len(luku) == 0:
                return
        except Exception:
            pass

        tulos = self.sovelluslogiikka.tulos - int(luku)
        self.sovelluslogiikka.aseta_arvo(tulos)


class Nollaus:
    def __init__(self, logiikka) -> None:
        self.sovelluslogiikka = logiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()


class Kumoa:
    #miksi pitäsi tietää, mikä komento suoritettiin viimeiseksi?
    def __init__(self, logiikka) -> None:
        self.sovelluslogiikka = logiikka

    def suorita(self):
        tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.edellinen_arvo)
        self.sovelluslogiikka.edellinen_arvo = tulos
