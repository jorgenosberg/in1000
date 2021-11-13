'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: testDato.py

KLAR FOR RETTING!

Dette programmet skal teste om klassen Dato fra "dato.py" fungerer som
den skal – med en prosedyre som inneholder kall på instansmetodene.

'''

from dato import Dato
import datetime as dt

### OPPGAVE 4.3 ###

def hovedprogram():
    # a
    # Oppretter en instans av Dato-klassen med 15. april 1998 som dato
    dato = Dato(15, 4, 1998)

    # b
    # Skriver ut hvilket år instansen har til terminalen
    print(dato.sjekkAar())

    # c
    # Sjekker om dagen er 15. eller 1. og skriver ut beskjedene fra oppgaveteksten
    if dato.sjekkDag(15) == True:
        print("Loenningsdag!")
    elif dato.sjekkDag(1) == True:
        print("Ny maaned, nye muligheter!")

    # d og e
    # Bruker formaterDato()-metoden for å skrive ut en formatert OG oversatt streng med datoen
    print(f"Datoen er {dato.formaterDato()}")

    # f
    # Bruker nesteDag()-metoden for å legge til 1 dag 
    dato.nesteDag()
    # Skriver ut den formaterte og oversatte datoen på nytt
    print(f"Datoen er nå {dato.formaterDato()}")

    # g
    # Leser inn en ny dato, parser den som et datetime-objekt og sjekker hvilken dato som kommer først
    ny_dato = input('Skriv inn en ny dato i formatet "YYYY-MM-DD". Eksempel: "1971-04-27".\nDin dato: ')
    dato.sjekkRekkefolge(ny_dato)

hovedprogram()