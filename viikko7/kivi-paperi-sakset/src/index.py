from kps import KPS
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from toinen_ihminen import ToinenIhminen

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = luo_peli(vastaus)

        if not peli: break

        peli.pelaa()

def luo_peli(vastaus):
    if vastaus.endswith("a"):
        return KPS(ToinenIhminen())
    elif vastaus.endswith("b"):
        return KPS(Tekoaly())
    elif vastaus.endswith("c"):
        return KPS(TekoalyParannettu(10))
    else:
        False

if __name__ == "__main__":
    main()
