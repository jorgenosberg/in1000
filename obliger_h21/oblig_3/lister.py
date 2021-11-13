'''
Oblig 3 | IN1000 | Høst 2021

Filnavn: lister.py

KLAR FOR RETTING!

I denne oppgaven skal jeg vise at jeg har forstått lister og list.methods().
Jeg bruker én egendefinert funksjon som er inkludert i toppen av dokumentet.

'''

### PROSEDYRER OG FUNKSJONER ###

# Funksjon (til oppgave 1.4)
def multiplyList(my_list):
    r = 1
    for x in my_list:
        r = r * x
    return r  

### OPPGAVE 1.1 ###

# Hente random-environmentet for å få tilfeldige tall
import random
from random import randint

# Lage en liste med tilfeldige tresifrede tall
en_liste = random.sample(range(50, 750), 3)

# Skrive ut resultatet
print(en_liste)

# Legge til et nytt tilfeldig tall
en_liste.append(randint(750, 1500))

# Skrive ut det første og tredje elementet
print(en_liste[0], en_liste[2])

### OPPGAVE 1.2 ###

# Lage en tom liste
ny_liste = []

# Be om 4 navn fra brukeren og legge dem inn
for i in range(0, 4):
    navn = input("Vennligst oppgi et navn: ").capitalize()
    ny_liste.append(navn)

### OPPGAVE 1.3 ###

# Sjekk om navnet mitt er i listen
if "Jørgen" in ny_liste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

### OPPGAVE 1.4 ###

# Lag ny liste med sum og produktet av den første listen
enda_en_liste = [sum(en_liste), multiplyList(en_liste)] # prod-funksjonen er definert øverst i dokumentet

    # Selv hadde jeg nok ikke giddet å definere funksjonen selv, men
    # ville heller ha brukt en prod-funksjon fra f.eks. math-biblioteket. 
    # Det ville ha sett slik ut:

# import math
# enda_en_liste = [sum(en_liste), math.prod(en_liste)]

# Slå sammen den første listen og den nye
det_var_da_veldig_mange_lister = en_liste
det_var_da_veldig_mange_lister.extend(enda_en_liste)

# Skrive ut den nye listen
print(det_var_da_veldig_mange_lister)

# Fjerne de to siste elementene
det_var_da_veldig_mange_lister.pop(-1)
det_var_da_veldig_mange_lister.pop(-1)

# Skriv ut listen på nytt
print(det_var_da_veldig_mange_lister)