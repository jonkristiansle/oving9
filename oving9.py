from datetime import datetime

class Avtale:
    def __init__(self, tittel, sted, tidspunkt, varighet):
        self.tittel = tittel # En streng
        self.sted = sted     # En streng
        self.tidspunkt = tidspunkt  # Et objekt
        self.varighet = varighet    # Et integer

    def __str__(self):
        return f"Avtalen er: {self.tittel}.\nSted: {self.sted}.\n\
            Tidspunkt: {self.tidspunkt}. Varighet: {self.varighet}"
    
def avtale():
    tittel = str(input("Hva er avtale emne? "))
    sted = str(input("Hvor skal avtalen skje? "))
    dato = input("Når er avtalen? Skriv på denne måten: ÅÅÅÅ-MM-DD TT:MM:SS ")
    tidspunkt = datetime.fromisoformat(dato)
    varighet = int(input("Hvor mange minutter skal avtalen vare? "))
    avtale = Avtale(tittel, sted, tidspunkt, varighet)
    return avtale

liste_med_avtaler = []
def skriv_ut_avtaler(lister):
    print("########## AVTALER ##########")
    for i in lister:
        print(f"Avtale {i}. {lister[i]}")

####### USIKKER PÅ DENNE ##########
def lagrer_liste_med_avtaler(lister): # Skal lagre listen med avtaler som ei txt.fil
    with open("liste_med_avtaler.txt", "w", encoding="UTF8") as lmf:
        lmf.write(lister)
###################################

### TESTING AV OPPGAVEN ###
avtale()
skriv_ut_avtaler(liste_med_avtaler)
lagrer_liste_med_avtaler(liste_med_avtaler)