from datetime import datetime
import csv


# OPPGAVE D & E
class Avtale:
    def __init__(self, tittel, sted, tidspunkt, varighet):
        self.tittel = tittel  # En streng
        self.sted = sted  # En streng
        self.tidspunkt = tidspunkt  # Et objekt
        self.varighet = varighet  # Et integer

    def __str__(self):
        return f"Avtalen er: {self.tittel}; Sted: {self.sted}; Tidspunkt: {self.tidspunkt}; skoVarighet: {self.varighet}"


# OPPGAVE F
def avtale(liste):
    tittel = str(input("Skriv inn tittel: "))
    sted = str('Skolen')
    dato = input("Skriv inn dato: ")
    tidspunkt = datetime.fromisoformat(dato)
    varighet = int(120)
    avtalen = Avtale(tittel, sted, tidspunkt, varighet)
    liste.append(avtalen)
    return tidspunkt, tittel
# 2022-11-04 12:00:00
# 2022-11-05 12:00:01


# Skriver ut avtalene til brukeren # OPPGAVE G
def skriv_ut_avtaler(lister):
    print("########## AVTALER ##########")
    for i in lister:
        print(i)


# lager en txt fil med avtalene som er oppgitt # OPPGAVE H
def lagrer_liste_med_avtaler(lister):  # Skal lagre listen med avtaler som ei txt.fil
    with open("liste_med_avtaler.txt", "w", encoding="UTF8") as lmf:
        for i in lister:
            lmf.write(str(i))
            lmf.write("\n")


# henter avtalene fra en fil # OPPGAVE I
def henter_avtale_fra_fil(filnavn):
    with open(filnavn, "r", encoding="UTF8") as fila:
        liste_fra_fil = []
        for e in csv.reader(fila, delimiter=";"):
            liste_fra_fil.append(e)
    print(liste_fra_fil)
    return liste_fra_fil


# finner avtaler med samme dato # OPPGAVE J
def samme_dato(liste, dato):
    for e in range(len(liste)):
        if dato in str(liste[e]):
            print(liste[e])


# Finner samme tittel # OPPGAVE K
def samme_tittel(liste, tittel):
    for e in range(len(liste)):
        if tittel in str(liste[e]):
            print(liste[e])


liste_med_avtaler = []
avtale(liste_med_avtaler)
avtale(liste_med_avtaler)
skriv_ut_avtaler(liste_med_avtaler)
lagrer_liste_med_avtaler(liste_med_avtaler)
henter_avtale_fra_fil("liste_med_avtaler.txt")
samme_dato(liste_med_avtaler, '2022-11-04')
