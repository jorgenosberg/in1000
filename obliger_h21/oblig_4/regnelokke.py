'''
Oblig 4 | IN1000 | Høst 2021

Filnavn: regnelokke.py

KLAR FOR RETTING!

Dette programmet skal bruke en while-løkke for å lagre input fra brukeren
frem til brukeren taster riktig tall.

Programmet skal deretter gjøre noen utregninger på den lagrede inputen,
blant annet en summeringsfunksjon og en egen utgave av max() og min()-funksjonene. 

'''

### OPPGAVE 2.1-2.2 ###

# Lage while-løkke frem til brukeren taster 0
tall = 1

min_liste = []

while tall != 0:
    tall = int(input("Velg et tall mellom 0 og 10: "))
    min_liste.append(tall) # Legge inn hvert tall i listen vha. append()-method

### OPPGAVE 2.3 ###

# Lag en for-løkke som skriver ut hvert element
for num in min_liste:
    print(num)

### OPPGAVE 2.4 ###

# Legg til variabelen minSum og summer listen
minSum = 0

for num in min_liste:
    minSum += num

print(minSum)

### OPPGAVE 2.5 ###

# Lag en for-løkke for å finne det minste tallet
minste_tall = min_liste[0]

for num in min_liste:
    if num < minste_tall:
        minste_tall = num

print(minste_tall)

# Lage en for-løkke for å finne det største tallet
største_tall = min_liste[0]

for num in min_liste:
    if num > største_tall:
        største_tall = num

print(største_tall)