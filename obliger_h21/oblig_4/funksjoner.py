'''
Oblig 4 | IN1000 | Høst 2021

Filnavn: funksjoner.py

KLAR FOR RETTING!

Dette programmet skal lage en adderingsfunksjon og 
en funksjon som teller antall ganger en gitt bokstav
forekommer i et ord.

'''

### OPPGAVE 1.1 ###

# Definere summeringsfunksjonen adder()
def adder(tall1, tall2):
    return tall1 + tall2

# Kalle på funksjonen
adder(77, 49)
adder(989, 69)

### OPPGAVE 1.2 ###

# # Be om string og bokstav fra brukeren
# tekststreng = input("Skriv en valgfri setning eller et lengre ord: ")
# bokstav = input("Skriv inn én enkelt bokstav: ")

# # Bruke en for-løkke for å telle antall forekomster av bokstaven
# antall = 0
# 
# for i in tekststreng:
#     if bokstav in tekststreng:
#         antall += 1

# # Skrive ut resultatet
# print(antall)

### OPPGAVE 1.3 ###

# Definere funksjonen tellForekomst()
def tellForekomst(min_tekst = input("Skriv en valgfri setning eller et lengre ord: "),
                  min_bokstav = input("Skriv inn én enkelt bokstav: ")):
    
    antall = 0
    
    for i in min_tekst:
        if min_bokstav in min_tekst:
            antall += 1
    
    print(antall)

# Kalle funksjonen
tellForekomst()

