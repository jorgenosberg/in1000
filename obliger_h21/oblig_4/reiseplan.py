'''
Oblig 4 | IN1000 | Høst 2021

Filnavn: reiseplan.py

KLAR FOR RETTING!

Dette programmet skal bruke lister og nøstede lister for å lage en oversiktlig reiseplan
for brukeren. Brukeren skal oppgi fem steder, fem klesplagg og fem avreisedatoer som skal
lagres i tre separate lister. Disse listene skal deretter nøstes sammen i en reiseplan 
brukeren kan konsultere.

Jeg bruker for-løkker og if-else-tester for å oppnå ønsket resultat.

'''

### OPPGAVE 3.1 ###

# Lag en tom liste og fyll den med 5 reisemål fra brukeren
steder = []

for x in range(0, 5):
    steder.append(input("Skriv inn et reisemål: ").capitalize())

### OPPGAVE 3.2 ###

# Lag to nye lister, klesplagg og avreisedatoer
klesplagg = []
avreisedatoer = []

# Hente input fra brukeren for begge lister
for x in range(0, 5):
    klesplagg.append(input("Skriv inn et klesplagg: ").capitalize())
    
for x in range(0, 5):
    avreisedatoer.append(input("Skriv inn en avreisedato: "))

### OPPGAVE 3.3 ###

# Lag en liste, reiseplan, som inneholder både steder, klesplagg og avreisedatoer
reiseplan = [steder, klesplagg, avreisedatoer]

### OPPGAVE 3.4 ###

# Skrive ut hele reiseplan og se at det blir tre lister
for element in reiseplan:
    print(element)

### OPPGAVE 3.5 ###

# Hente input fra brukeren for å velge en av de tre listene
liste_indeks1 = int(input("Oppgi et tall mellom 0 og 2 for å velge en av listene: "))

# Hente input fra brukeren for å velge et av de fem elementene i den valgte listen
liste_indeks2 = int(input("Oppgi et tall mellom 0 og 4 for å velge et av elementene i listen: "))

# Sjekk om tallet er gyldig
if liste_indeks1 not in range(0, 3) or liste_indeks2 not in range(0, 5):
    print("Ugyldig input!")
else:
    print(reiseplan[liste_indeks1][liste_indeks2])