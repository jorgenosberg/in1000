'''
Oblig 3 | IN1000 | Høst 2021

Filnavn: ordbok.py

KLAR FOR RETTING!

Dette programmet skal vise at jeg har forstått bruken av ordbøker (dictionaries) og kan 
manipulere innholdet i dem. 

Ordboken jeg skal lage er en vareliste som må inneholde følgende varer:
- Melk: 14.90
- Brød: 24.90
- Yoghurt: 12.90
- Pizza: 39.90

'''

### OPPGAVE 2.1 ###

# Opprette ordboken med varene fra oppgaveteksten
butikkvarer = {
    "Melk": 14.90,
    "Brød": 24.90,
    "Yoghurt": 12.90,
    "Pizza": 39.90
}

# Skrive ut ordboken
print(butikkvarer)

### OPPGAVE 2.2 ###

# Legge inn to varer fra brukeren
print("Du vil nå bli bedt om å oppgi navnet og prisen på to varer.")

for x in range(0, 2):
    vare = input("Navnet på varen: ").capitalize()
    pris = float(input("Prisen på varen: "))
    butikkvarer[vare] = pris

# Skriv ut på nytt
print(butikkvarer)

