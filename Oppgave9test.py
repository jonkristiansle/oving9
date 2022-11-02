from datetime import datetime
import csv


class Avtale:
    def __init__(self, tittel, sted, tidspunkt, varighet):
        self.tittel = tittel  # En streng
        self.sted = sted  # En streng
        self.tidspunkt = tidspunkt  # Et objekt
        self.varighet = varighet  # Et integer

    def __str__(self):
        return f"Avtalen er: {self.tittel};Sted: {self.sted}.;Tidspunkt: {self.tidspunkt}.;Varighet: {self.varighet}"


def avtale(liste):
    tittel = str('skole')
    sted = str('Skolen')
    dato = '2022-11-04 12:00:00'
    tidspunkt = datetime.fromisoformat(dato)
    varighet = int(120)
    avtalen = Avtale(tittel, sted, tidspunkt, varighet)
    liste.append(avtalen)


#2022-11-04 12:00:00


def skriv_ut_avtaler(lister):
    print("########## AVTALER ##########")
    for i in lister:
        print(i)


####### USIKKER PÅ DENNE ##########
def lagrer_liste_med_avtaler(lister):  # Skal lagre listen med avtaler som ei txt.fil
    with open("liste_med_avtaler.txt", "w", encoding="UTF8") as lmf:
        for i in lister:
            lmf.write(str(i))


def henter_avtale_fra_fil(filnavn):
    with open(filnavn, "r", encoding="UTF8") as fila:
        liste_fra_fil = []
        for e in csv.reader(fila, delimiter=";"):
            liste_fra_fil.append(e)
    print(liste_fra_fil)
    return liste_fra_fil


liste_med_avtaler = []
avtale(liste_med_avtaler)
skriv_ut_avtaler(liste_med_avtaler)
lagrer_liste_med_avtaler(liste_med_avtaler)
henter_avtale_fra_fil("liste_med_avtaler.txt")
