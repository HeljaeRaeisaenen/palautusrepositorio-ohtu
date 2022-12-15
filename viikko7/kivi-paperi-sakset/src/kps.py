from tuomari import Tuomari


class KPS:
    def __init__(self, toinen_pelaaja) -> None:
        self.toinen_pelaaja = toinen_pelaaja

    def pelaa(self, ):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.toinen_pelaaja.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self.toinen_pelaaja.anna_siirto()

            self.toinen_pelaaja.valittu_siirto_tieto(tokan_siirto
            )
            print(f"Tietokone valitsi: {tokan_siirto}")
            self.toinen_pelaaja.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
