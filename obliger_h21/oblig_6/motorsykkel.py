'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: motorsykkel.py

KLAR FOR RETTING!

Dette programmet skal definere en klasse "Motorsykkel" med
nødvendige instansvariabler og metoder.

Klassen skal ha en konstruktør som setter instansvariablene, én
metode som "kjører" og øker km-standen, én metode som returnerer
km_standen og én metode som skriver ut informasjon om motorsykkelen. 
'''

### OPPGAVE 1.1-1.4 ###

class Motorsykkel:
    # Definere attributes for Motorsykkel vha. __init__-metoden
    def __init__(self, merke, reg_nummer, km_stand):    
        self._merke = merke
        self._reg_nummer = reg_nummer
        self._km_stand = km_stand

    # Definere en ny metode som øker km_stand med et gitt antall km
    def kjor(self, km):
        self._km_stand += km

    # Metode som returnerer km_stand
    def hentKilometerstand(self):
        return self._km_stand

    # Metode som skriver ut attributes på en ryddig og oversiktlig måte vha. f-strings
    def skrivUt(self):
        print(f"Motorsykkelen har merket {self._merke}.")
        print(f"Registreringsnummeret er {self._reg_nummer}.")
        print(f"Kjøretøyet har kjørt {self._km_stand} kilometer totalt.")