'''
Lag et program som tar in tre verdier: en string, et heltall og et flyttall, og lagrer dem i tre variabler.

a) Skriv ut de verdiene og typene til de tre variablene. Bruk rigtige funksjonen til å sjekke datatypene.

b) Forklar om programmet vil kjøre eller krasje i følgende scenarier:
- Med tastatur-input string: " ", heltall: 0, flyttall: 3.8
- Med tastatur-input string: 1, heltall: 2, flyttall: 3
- Med tastatur-input string: 1, heltall: -0, flyttall: 3.8
- Med tastatur-input string: 3.8, heltall: 3.8, flyttall: 3.8

Prøv å kjøre programmet selv for å teste om du hadde rett

c) Prøv følgende tre scenarier:
- multipliser heltallet med stringen
- multipliser heltallet med flyttallet
- multipliser stringen med flyttallet

Forklar hva som skjer, og prøv å skrive ut typen av resultatet.

d) Hva skjer når vi konverterer et flyttall til et heltall?
Skriv ut resultatet, og prøv å kjøre programmet med flere forskjellige flyttaller.
'''

# Lag tre variabler
s = "Hei"
n = 15
f = 3.8

# Skriv ut verdiene og typene
print(s)
print(type(s))

print(n)
print(type(n))

print(f)
print(type(f))
