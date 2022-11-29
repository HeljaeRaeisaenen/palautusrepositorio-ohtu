from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka


def main():

    window = Tk()
    window.title("Laskin")
    sovellus = Sovelluslogiikka()

    kayttoliittyma = Kayttoliittyma(sovellus, window)

    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
