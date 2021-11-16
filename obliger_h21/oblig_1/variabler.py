'''
Oblig 1 | IN1000 | Høst 2021

Filnavn: variabler.py

Dette programmet er svaret på første oppgave i obligen,
og skal vise at jeg kan bruke print()- og input()-funksjonene samt
gjøre grunnleggende string-manipulasjon og utregninger.
'''

### Hilse på en student ###

# Jeg vil skrive ut teksten "Hei Student!"
print("Hei Student!")

# Jeg vil innhente brukerens navn for dermed å kunne skrive "Hei" + "navn"
navn = input("Hva heter du? ")

# Jeg bruker en formatert string for å skrive ut {navn}-variabelen
print(f"Hei, {navn}!")

# En mer basic løsning ville være standard string concatenation
# print("Hei, " + navn + "!")

### Gjøre utregninger med to heltall (integer) ###

# Opprette to tallvariabler
num1 = 91
num2 = 17

# Vise de to tallverdiene i terminalen
print(num1)
print(num2)

# Beregne differansen
differanse = num1 - num2

# Skrive ut resultatet
print(f"Differanse: {differanse}.")

### Legge sammen to strings ###

# Be om nytt navn fra bruker
nytt_navn = input("Oppgi et nytt navn: ")

# Kombiner de to navnene til en ny variabel
sammen = navn + nytt_navn

# Skrive ut 'sammen' til terminalen
print(sammen)

# Fikse variabelen 'sammen'
sammen = f"{navn} og {nytt_navn}"

print(sammen)