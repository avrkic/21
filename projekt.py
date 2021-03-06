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

    def pobjeda(self):
        self.ukupno += self.ulog

    def poraz(self):
        self.ukupno -= self.ulog

def provjera_beta(zetoni):
    while True:
        try:
            zetoni.ulog = int(input("Koliko zelite uloziti?"))
        except ValueError:
            print("Mora biti broj")
        else:
            if zetoni.ulog > zetoni.ukupno:
                print("Nemas dovoljno, imas: ",zetoni.ukupno)
            else:
                break

#hitanje
def udari (spil,ruka):
    ruka.dodaj_kartu(spil.dili())
    ruka.primjena_asova_()

# odabir hit or stay


def udari_ili_ostani(spil,ruka,zetoni):
    global igrase
    as_za_double =False
    while True:
        for i in range(len(ruka.karte)):
            if ruka.karte[i].naziv == 'A':
                as_za_double = True

        provjera_double = ((ruka.vrijednost > 8 and ruka.vrijednost < 12) or (as_za_double and (ruka.vrijednost - 10 > 8 and ruka.vrijednost - 10 < 12))) and zetoni.ulog <= (zetoni.ukupno - zetoni.ulog)

        if provjera_double:
            odabir = input("Hoces li udariti ili ostati ili duplati? 'u' ili 'o' ili 'd'")

            if odabir[0].lower() == 'u':
                udari(spil, ruka)  # pozivam udarac

            elif odabir[0].lower() == 'o':
                print("Ostao si. Dilerov je red!")
                igrase = False
            elif odabir[0].lower() == 'd':
                print("Duplao si dilerov red!")
                zetoni.ulog += zetoni.ulog
                udari(spil, ruka)
                igrase = False
            else:
                print("Error pokusaj opet")
                continue
            break

        else:
            odabir = input("Hoces li udariti ili ostati? 'u' ili 'o'")

            if odabir[0].lower() == 'u':
                udari(spil,ruka)   #pozivam udarac

            elif odabir[0].lower() == 'o':
                print("Ostao si. Dilerov je red!")
                igrase = False

            else:
                print("Error pokusaj opet")
                continue
            break

#Pokazivanje karata

def pokazi_pocetno(igrac,diler):
    print('Dilerova ruka: Neotkrivena karta i', diler.karte[0].zog + diler.karte[0].naziv)
    duz = len(igrac.karte)
    igraceva_ruka = ''
    for i in range(duz):
        igraceva_ruka += igrac.karte[i].zog + igrac.karte[i].naziv + ' '
    print("\nIgraceva ruka: " + igraceva_ruka)

def pokazi_sve(igrac,diler):
    dilerova_ruka1 = ''
    duz_dilera = len(diler.karte)
    for i in range(duz_dilera):
        dilerova_ruka1 += diler.karte[i].zog + diler.karte[i].naziv + ' '
    print("\nDilerova ruka", dilerova_ruka1, "\n")
    print("Dilerov zbroj", diler.vrijednost)
    duz1 = len(igrac.karte)
    igraceva_ruka1 = ''
    for i in range(duz1):
        igraceva_ruka1 += igrac.karte[i].zog + igrac.karte[i].naziv + ' '
    print("\nIgraceva ruka:" + igraceva_ruka1)
    print("Zbroj igracevih karata: ", igrac.vrijednost)
    
#scenariji


def igrac_busta(igrac,diler,zetoni):
    print("Presli ste 21! Izgubili ste!")
    zetoni.poraz()


def igrac_pobjeduje(igrac,diler,zetoni):
    print("Pobjedili ste!")
    zetoni.pobjeda()


def diler_busta(igrac,diler,zetoni):
    print("Diler je presao 21! Dobili ste!")
    zetoni.pobjeda()

def diler_pobjeduje(igrac,diler,zetoni):
    print("Diler pobjeduje!")
    zetoni.poraz()


def push(igrac,diler):
    print("Izjednaceni ste! Vracaju vam se vasi ulozi!")


#Igramo

#print
pi = PrikazIgre()
pi.pikaziPocetakIgre()

# igrac zetoni
igracevi_zetoni = Zetoni()

ime_igraca=""
while ime_igraca == "":
    ime_igraca = input("Unesite zeljeno korisnicko ime: ")

try:
    igracevi_zetoni.ukupno = (int)(input("Sa koliko zetona zelite uci"))
except:
    print("Niste unijeli valjan broj te vam je dodjeljeno 100")




while True:
    #Stvori misaj
    spil = Spil()
    spil.misaj()
    #Igrac ruka
    igraca = Ruka()
    igraca.dodaj_kartu(spil.dili())
    igraca.dodaj_kartu(spil.dili())
    #Diler ruka
    diler = Ruka()
    diler.dodaj_kartu(spil.dili())
    diler.dodaj_kartu(spil.dili())

    #Igrac ulog
    provjera_beta(igracevi_zetoni)

    #Karte sa dilerovom sakrivenom
    pokazi_pocetno(igraca,diler)
    while igrase:  #pozivam hit or stay

        #izbor
        udari_ili_ostani(spil,igraca,igracevi_zetoni)

        #pokazi kartu sa dilerovom sakrivenom
        pokazi_pocetno(igraca, diler)

        #ako je priko 21 pokrecemo bust i gasim petlju
        if igraca.vrijednost > 21:
            igrac_busta(igraca,diler,igracevi_zetoni)

            break


    #ako igrac nije busta diler hita do 17
    if igraca.vrijednost <=21:

        while diler.vrijednost<17:
            udari(spil,diler)
            diler.primjenaasova()

        #pokazi sve karte
        pokazi_sve(igraca,diler)

        #provjere scenarija

        if diler.vrijednost >21:
            diler_busta(igraca,diler,igracevi_zetoni)
        elif diler.vrijednost > igraca.vrijednost:
            diler_pobjeduje(igraca,diler,igracevi_zetoni)
        elif diler.vrijednost < igraca.vrijednost:
            igrac_pobjeduje(igraca,diler,igracevi_zetoni)
        else:
            push(igraca,diler)

    #Koliko je igracu ostalo zetona
    print("\n"+ ime_igraca + " ostalo vam je : ",igracevi_zetoni.ukupno)
    if igracevi_zetoni.ukupno == 0:
        print("Izgubili ste!")
        exit()
    else:
        #Os opet igrat
        nova_igra = input("Zelite li ponovno igrati? Unesite 'D' ili 'N' ")
        if nova_igra[0].lower() == 'd':
            igrase = True
            continue
        else:
            print("Ispratit ce vas zastitar!")
            break
