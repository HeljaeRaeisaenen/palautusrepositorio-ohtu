from kps import KPS

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
        return KPS.luo_kaksinpeli()
    elif vastaus.endswith("b"):
        return KPS.luo_yksinpeli()
    elif vastaus.endswith("c"):
        return KPS.luo_vaikea_yksinpeli()
    else:
        False

if __name__ == "__main__":
    main()
