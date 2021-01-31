import random
igrase = True

class PrikazIgre (object):
    def pikaziPocetakIgre(self):
        print("*" * 50)
        print("*" * 20 + "IGRA 21" + "*" * 20)
        print("*" *50)


class Karta(object):
    __karta_info = {1: ('A', 11),
                    2: ('2', 2),
                    3: ('3', 3),
                    4: ('4', 4),
                    5: ('5', 5),
                    6: ('6', 6),
                    7: ('7', 7),
                    8: ('8', 8),
                    9: ('9', 9),
                    10: ('10', 10),
                    11: ('J', 10),
                    12: ('Q', 10),
                    13: ('K', 10),
                    }
    __zogovi = ["♠","♥","♣","♦"]

    @staticmethod
    def brojevi():
        return Karta.__karta_info.keys()

    @staticmethod
    def zogovi():
        return list(Karta.__zogovi)

    def __init__(self, broj, zog, snaga, naziv):
        self.__broj = broj
        self.__zog = zog
        self.__snaga = snaga
        self.__naziv = naziv

    @property
    def broj(self):
        return self.__broj

    @property
    def zog(self):
        return self.__zog

    @property
    def naziv(self):
        return Karta.__karta_info[self.__broj][0]

    @property
    def snaga(self):
        return Karta.__karta_info[self.__broj][1]


class Igrac:
    def __init__(self, ime):
        self.__ime = ime

    def ime(self):
        return Igrac.__ime


class Spil:
    def __init__(self):
        self.spil = []   # zapocinjem praznom
        for z in Karta.zogovi():
            for v in Karta.brojevi():
                #for i in range(4): #spil se sastoji od 4 deka
                    self.spil.append(Karta(v,z,Karta.snaga,Karta.naziv)) #pokusavam pravit kartu i dodat je u listu


    def misaj(self):
        random.shuffle(self.spil)

    def dili(self):
        jedna_karta= self.spil.pop()
        return jedna_karta


class Ruka:
    def __init__(self):
        self.karte = []  #prazna ruka
        self.vrijednost = 0 #pocetni zbroj je 0
        self.br_asova = 0 #brojac aseva

    def dodaj_kartu(self,karta):
        self.karte.append(karta)
        self.vrijednost += karta.snaga
        if karta.snaga == 11:
            self.br_asova +=1

    def primjena_asova_(self):
        while self.vrijednost > 21 and self.br_asova:
            self.vrijednost-=10
            self.br_asova-=1


class Zetoni:
    def __init__(self):
        self.ukupno = 100
        self.ulog = 0
