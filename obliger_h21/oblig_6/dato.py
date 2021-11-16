'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: dato.py

KLAR FOR RETTING!

Dette programmet svarer på oppgave 4 i obligen. I koden skal jeg opprette en 
klasse "Dato" med parametrene nyDag, nyMaaned og nyttAar. Klassen skal ha
metoder som både kan returnere året, lage en lesevennlig streng av datoen, sjekke
om datoen er en gitt dag, sjekk om datoen kommer før eller etter en gitt dato, 
og endre datoen til neste dag.

Ekstra: For å skrive ut en lettlest utgave av datoen vil jeg bruke oversettelses-
funksjonen (engToNor()) jeg definertere i oblig 5.

'''
# Importere datetime-biblioteket for å jobbe med dato-objekter
import datetime as dt

# Limer inn oversettelsesfunksjonen jeg laget i filen temperatur.py fra oblig 5. OBS: Return er modifisert for å inkludere år.
def engToNor(dato):
    dager = {"Monday":"mandag", "Tuesday":"tirsdag", "Wednesday":"onsdag",
             "Thursday":"torsdag", "Friday":"fredag", "Saturday":"lørdag", "Sunday":"søndag"}
    måneder = {"Jan":"januar", "Feb":"februar", "Mar":"mars", "Apr":"april",
               "May":"mai", "Jun":"juni", "Jul":"juli", "Aug":"august", "Sep":"september",
               "Oct":"oktober", "Nov":"november", "Dec":"desember"}
    return f"{dager[dato.split()[0]]} {dato.split()[1]} {måneder[dato.split()[2]]} {dato.split()[3]}"

### OPPGAVE 4.1 og 4.2 a-e ###
 
class Dato:
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._dag = nyDag
        self._maaned = nyMaaned
        self._aar = nyttAar
        self.dato = dt.datetime(nyttAar, nyMaaned, nyDag) # Lager en egen attribute med et datetime-objekt

    def sjekkAar(self):
        return self._aar
    
    def formaterDato(self):
        return engToNor(self.dato.strftime("%A %d. %b %Y")) # Bruker oversettelsesfunksjonen og strftime for å formatere

    def sjekkDag(self, dag):
        if dag == self._dag:
            return True
    
    def sjekkRekkefolge(self, dato):
        liste = dato.split("-")
        dato = dt.datetime(int(liste[0]), int(liste[1]), int(liste[2])) # Lager nytt datetime-objekt med den splittede datoen fra input
        if dato < self.dato:
            print("Denne datoen kommer før datoen du oppga.")
        elif dato == self.dato:
            print("Datoene er helt like.")
        else:
            print("Denne datoen kommer etter datoen du oppga.")
    
    def nesteDag(self):
        self.dato += dt.timedelta(days = 1) # Fordi jeg bruker datetime funker denne til alle datoer og alle år :)