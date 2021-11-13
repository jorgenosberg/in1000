'''
Oblig 5 | IN1000 | Høst 2021

Filnavn: regnefunksjoner.py

KLAR FOR RETTING!

Dette programmet skal lage fire basic regnefunksjoner, en for
addisjon, en for subtraksjon, en for divisjon og en for konvertering
fra tommer til centimeter.

Deretter skal programmet sjekke at alle funksjonene funker vha.
assert-tester.

Til slutt skal programmet lage en prosedyre skrivBeregninger() som bruker
de definerte funksjonene for å ta inn verdier og skrive ut resultatene
på en oversiktlig måte.
'''

### OPPGAVE 1 ###

# Definere addisjon() med 2 parametre
def addisjon(param1, param2):
    return param1 + param2

# Teste funksjonen med to heltall
print(addisjon(24, 76))

### OPPGAVE 2 ###

# Definere subtraksjon() med parametre
def subtraksjon(param1, param2):
    return param1 - param2

# Definere divisjon() med 2 parametre
def divisjon(param1, param2):
    return param1 / param2

# Teste addisjon() med assert
assert addisjon(49, 49) == 98
assert addisjon(300, -47) == 253
assert addisjon(-22, -198) == -220

# Teste subtraksjon() med assert
assert subtraksjon(49, 48) == 1
assert subtraksjon(-103, -20) == -83
assert subtraksjon(17, -17) == 34

# Teste divisjon() med assert
assert divisjon(4752, 66) == 72
assert divisjon(259, -5) == -51.8
assert divisjon(-65, -50) == 1.3

### OPPGAVE 3 ###

# Definere tommerTilCm() med parameteret antallTommer
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

# Teste funksjonen
print(tommerTilCm(24))

### OPPGAVE 4 ###

# # Definere prosedyren skrivBeregninger()
# def skrivBeregninger():
#     print("Utregninger")
    
#     # Hente inn to tall
#     tall1 = float(input("Skriv inn et tall: "))
#     tall2 = float(input("Skriv inn et tall: "))
    
#     # Bruke egne funksjoner og skrive ut
#     print(f"Resultat av addisjon: {addisjon(tall1, tall2)}")
#     print(f"Resultat av subtraksjon: {subtraksjon(tall1, tall2)}")
#     print(f"Resultat av divisjon: {divisjon(tall1, tall2)}")
    
#     print("Konvertering fra tommer til centimeter")
    
#     # Hente inn nytt tall
#     tall3 = float(input("Skriv inn et tall: "))
    
#     # Bruke tommerTilCm() og skrive ut
#     print(f"{round(tall3)} tommer tilsvarer ca. {tommerTilCm(tall3)} centimeter.")

# ### OPPGAVE 5 ###

# # Teste prosedyren fra oppg. 4
# skrivBeregninger()