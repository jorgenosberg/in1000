'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: testHund.py

KLAR FOR RETTING!

Dette programmet tester klassen Hund slik den ble definert
i filen hund.py. Prosedyren hovedprogram() skal opprette en
instans av klassen og teste metodene spring, spis og hentVekt().

Ekstra: Programmet skal også skrive ut tegningen av hunden ved å bruke
print(instans) og tegningen som er lagt inn i __repr__-metoden.

'''

# Importerer klassen Hund fra hund.py
from hund import Hund
from random import randint

# Definerer prosedyren
def hovedprogram():
    rex = Hund(10, 21) # Oppretter en hund "rex" som er 10 år gammel og veier 21 kg (typ labrador)

    for x in range(0, 3): # For-loop for å teste .spring() og .spis() tre ganger
        rex.spring() # Kaller på spring-metoden
        print(rex.hentVekt()) # Skriver ut vekten etter at rex har løpt
        rex.spis(randint(1, 25)) # Kaller på spis-metoden og legger inn random mengde mat
        print(rex.hentVekt()) # Skriver ut vekten etter at rex har spist
    
    print(f"\nRex er {rex}") # Skriver ut tegningen av en hund som jeg la inn i __repr__-metoden på en ny linje

# Kaller på prosedyren hovedprogram()
hovedprogram()