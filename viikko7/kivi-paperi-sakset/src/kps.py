from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from toinen_ihminen import ToinenIhminen

class KPS:
    def __init__(self, toinen_pelaaja):
        self.toinen_pelaaja = toinen_pelaaja

    @staticmethod
    def luo_yksinpeli():
        return KPS(Tekoaly())
    
    @staticmethod
    def luo_vaikea_yksinpeli():
        return KPS(TekoalyParannettu(10))
    
    @staticmethod
    def luo_kaksinpeli():
        return KPS(ToinenIhminen())

    def pelaa(self, ):
        tuomari = Tuomari()

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.toinen_pelaaja.anna_siirto()

        self.toinen_pelaaja.valittu_siirto_tieto(tokan_siirto)
        
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self.toinen_pelaaja.anna_siirto()

            self.toinen_pelaaja.valittu_siirto_tieto(tokan_siirto)
            self.toinen_pelaaja.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
