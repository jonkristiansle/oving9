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


def avtale():
    tittel = str(input("Hva er avtale emne? "))
    sted = str(input("Hvor skal avtalen skje? "))
    dato = input("Når er avtalen? Skriv på denne måten: ÅÅÅÅ-MM-DD TT:MM:SS ")
    tidspunkt = datetime.fromisoformat(dato)
    varighet = int(input("Hvor mange minutter skal avtalen vare? "))
    avtalen = Avtale(tittel, sted, tidspunkt, varighet)
    #liste.append(avtalen)
    return avtalen

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
            lmf.write('\n')


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
#avtale(liste_med_avtaler)
#avtale(liste_med_avtaler)
#skriv_ut_avtaler(liste_med_avtaler)
#lagrer_liste_med_avtaler(liste_med_avtaler)
#henter_avtale_fra_fil("liste_med_avtaler.txt")
#samme_dato(liste_med_avtaler,'2022-11-04')

def meny():
    operation = input('''
Select operation:
[1] Lese inn avtalve fra fil
[2] Skriv avtalene til fil
[3] Ny avtale
[4] Skriv ut alle avtalene
[5] Avslutt
[6] Slett avtale 
[7] Redigere avtale 

''')
    meny = []

    if operation == '1':
        henter_avtale_fra_fil('liste_med_avtaler.txt')
        igjen()
    elif operation == '2':
        lagrer_liste_med_avtaler(liste_med_avtaler)
        igjen()
    elif operation == '3':
        liste_med_avtaler.append(avtale())
        igjen()
    elif operation == '4':
        skriv_ut_avtaler(liste_med_avtaler)
        igjen()
    elif operation == '5':
        print('Ok, hadde :)')
    elif operation == '6':
        skriv_ut_avtaler(liste_med_avtaler)
        del liste_med_avtaler[int(input('Hvilken avtale vil du slette: '))-1]
        igjen()
    elif operation == '7':
        skriv_ut_avtaler(liste_med_avtaler)
        indeks=int(input("redigere"))
        #indeks = liste_med_avtaler[int(input('Hvilken avtale vil du redigere '))-1]
        liste_med_avtaler[indeks]= avtale()

        igjen()
    else:
        print('Du må velge et gyldig tall.')
        meny()

def igjen():
    list_again = input('''
Har du lyst til å gjøre flere endringer (J/N)
''')

    if list_again.upper() == 'J':
        meny()
    elif list_again.upper() == 'N':
        print('Ok, hadde :)')
    else:
        igjen()

meny()
#2022-11-04 12:00:00
samme_tittel(liste_med_avtaler,'skole')
