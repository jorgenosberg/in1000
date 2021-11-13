'''
Oblig 5 | IN1000 | Høst 2021

Filnavn: test.py

'''

# regnefunksjoner.py

### OPPGAVE 1.1 ### 

# Definert funksjonen addisjon()
def addisjon(param1, param2):
    return param1 + param2

# Teste og skrive ut resultatet
print(addisjon(24, 20))

### OPPGAVE 1.2 ###

# Definere funksjonene
def subtraksjon(param1, param2):
    return param1 - param2

def divisjon(param1, param2):
    return param1 / param2

assert addisjon(24, 20) == 44
assert addisjon(-24, -20) == -44
assert addisjon(-24, 20) == -4

# assert subtraksjon(24, 20) == 44
# assert subtraksjon(24, 20) == 44
# assert subtraksjon(24, 20) == 44

# assert divisjon(24, 20) == 44
# assert divisjon(24, 20) == 44
# assert divisjon(24, 20) == 44

### OPPGAVE 1.3 ###

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

print(round(tommerTilCm(100)))

### OPPGAVE 1.4 ###

def skrivBeregninger():
    print("Utregninger:")
    tall1 = float(input("Skriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall 2: "))
    print()
    print(f"Resultat av summering: {addisjon(tall1, tall2)}")
    print(f"Resultat av subtraksjon: {subtraksjon(tall1, tall2)}")
    print(f"Resultat av divisjon: {divisjon(tall1, tall2)}")
    print()
    print("Konvertering fra tommer til centimeter:")
    tall3 = float(input("Skriv inn et tall til: "))
    print(f"Resultat: {tommerTilCm(tall3)}")

### OPPGAVE 1.5 ###

skrivBeregninger()


### OPPGAVE 2.1 ###

