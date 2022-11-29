KAPASITEETTI = 5
OLETUSKASVATUS = 5

#good enough
class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, testattava):
        for alkio in self.lukujono:
            if testattava == alkio:
                return True

        return False

    def lisaa(self, lisattava):
        if not self.kuuluu(lisattava):
            self.lukujono[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                self.kasvata_lukujonoa()

            return True

        return False

    def poista(self, poistettava):
        kohta = -1
        apu = 0

        if not self.kuuluu(poistettava):
            return False
        
        for i in range(0, self.alkioiden_lkm):
            if poistettava == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        for i in range(kohta, self.alkioiden_lkm - 1):
            apu = self.lukujono[i]
            self.lukujono[i] = self.lukujono[i + 1]
            self.lukujono[i + 1] = apu

        self.alkioiden_lkm -= 1
        return True

    def kasvata_lukujonoa(self):
        taulukko_old = self.lukujono
        self.kopioi_taulukko(self.lukujono, taulukko_old)
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujono)

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        uusi_lista = [0] * self.alkioiden_lkm

        for i in range(0, self.alkioiden_lkm):
            uusi_lista[i] = self.lukujono[i]

        return uusi_lista

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_listana = a.to_int_list()
        b_listana = b.to_int_list()

        for alkio in a_listana:
            yhdiste_joukko.lisaa(alkio)

        for alkio in b_listana:
            yhdiste_joukko.lisaa(alkio)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        a_listana = a.to_int_list()
        b_listana = b.to_int_list()

        for a_alkio in a_listana:
            for b_alkio in b_listana:
                if a_alkio == b_alkio:
                    leikkaus_joukko.lisaa(b_alkio)

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_listana = a.to_int_list()
        b_listana = b.to_int_list()

        for alkio in a_listana:
            erotus_joukko.lisaa(alkio)

        for alkio in b_listana:
            erotus_joukko.poista(alkio)

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuloste = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuloste += str(self.lukujono[i])
                tuloste += ", "
            tuloste += str(self.lukujono[self.alkioiden_lkm - 1])
            tuloste += "}"
            return tuloste
