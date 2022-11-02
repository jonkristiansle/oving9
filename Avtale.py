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
            lmf.write('\n')


def henter_avtale_fra_fil(filnavn):
    with open(filnavn, "r", encoding="UTF8") as fila:
        liste_fra_fil = []
        for e in csv.reader(fila, delimiter=";"):
            liste_fra_fil.append(e)
    print(liste_fra_fil)
    return liste_fra_fil




liste_med_avtaler = []
#avtale(liste_med_avtaler)
#avtale(liste_med_avtaler)
#skriv_ut_avtaler(liste_med_avtaler)
#lagrer_liste_med_avtaler(liste_med_avtaler)
#henter_avtale_fra_fil("liste_med_avtaler.txt")
#samme_dato(liste_med_avtaler,'2022-11-04')

def list():
    operation = input('''
Select operation:
[1] Lese inn avtalve fra fil
[2] Skriv avtalene til fil
[3] Ny avtale
[4] Skriv ut alle avtalene fra fil
[5] Avslutt

''')
    mylist = []

    if operation == '1':
        skriv_ut_avtaler(liste_med_avtaler)

    elif operation == '2':
        lagrer_liste_med_avtaler(liste_med_avtaler)

    elif operation == '3':
        avtale(liste_med_avtaler)

    elif operation == '4':
        print('feil')
    elif operation == '5':
        print('Ok, hadde :)')
    else:
        print('Du må velge et gyldig tall.')
       if operation == '1'or'2'or'3'or'4':
            again()

def again():
    list_again = input('''
Har du lyst til å gjøre flere endringer (J/N)
''')

    if list_again.upper() == 'J':
        list()
    elif list_again.upper() == 'N':
        print('Ok, hadde :)')
    else:
        again()

list()