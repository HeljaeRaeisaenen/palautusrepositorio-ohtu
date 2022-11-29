class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo


class Summa:
    def __init__(self, logiikka, lue_syote) -> None:
        self.sovelluslogiikka = logiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
            if len(luku) == 0:
                luku = 0
        except Exception:
            pass
        
        self.sovelluslogiikka.tulos += int(luku)

class Erotus:
    def __init__(self, logiikka, lue_syote) -> None:
        self.sovelluslogiikka = logiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
            if len(luku) == 0:
                luku = 0
        except Exception:
            pass
        self.sovelluslogiikka.tulos -= int(luku)

class Nollaus:
    def __init__(self, logiikka, lue_syote) -> None:
        self.sovelluslogiikka = logiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovelluslogiikka.tulos = 0

class Kumoa:
    def __init__(self, logiikka, lue_syote) -> None:
        self.sovelluslogiikka = logiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
        except Exception:
            pass
        