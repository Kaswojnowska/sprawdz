#gotowa klasa Pojazd

class Pojazd:

    def __init__(self, kolor, rodzaj, wartosc, nazwa):
        self.kolor = kolor
        self.rodzaj = rodzaj
        self.wartosc = wartosc
        self.nazwa = nazwa
        
    def opis(self):
        napis_opisu = ("%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc))
        return napis_opisu

# sprawdzenie kodu
if __name__ == '__main__':
    Auto1 = Pojazd("czerwony","kabriolet", 60000, "Ferarri")
    Auto2 = Pojazd("niebieski", "autobus", 10000, "Ikarus")
    print (Auto1.opis())
    print (Auto2.opis()) 