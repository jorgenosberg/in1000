'''
Oblig 5 | IN1000 | Høst 2021

Filnavn: uio_brukere.py

KLAR FOR RETTING!

Dette programmet skal lage tre funksjoner. Én som kan generere
brukernavn fra et gitt navn, én som genererer e-post-adresser 
vha. et brukernavn og et e-post-suffiks, og én som itererer over
en ordbok og skriver ut e-postadressene.

Til slutt skal disse tre funksjonene implementeres i en løkke
der brukeren kan oppgi navn og ønsket e-post-suffiks for alle
brukerne hen ønsker, og deretter få oppgitt passende adresser
for hver av dem.
'''

### OPPGAVE 1 ###

# Definere lagBrukernavn() for å gjøre om vanlig navn (tekststreng) til et UiO-brukernavn
def lagBrukernavn(navn):  
    
    # Sjekk at brukeren har tastet inn to navn med mellomrom
    if len(navn.split()) != 2:
        print('Feil input! Du kan bare bruke fornavn og siste etternavn, adskilt med mellomrom. Eksempel: "Kari Nordmann".')
    else:
        # For-løkke for å fikse norske bokstaver hvis de dukker opp
        for letter in navn:
            if letter.lower() == "æ":
                i = navn.index(letter)
                navn = navn[0:i] + "ae" + navn[i + 1: ]
            elif letter.lower() == "ø":
                i = navn.index(letter)
                navn = navn[0:i] + "o" + navn[i + 1: ]
            elif letter.lower() == "å":
                i = navn.index(letter)
                navn = navn[0:i] + "a" + navn[i + 1: ]
        return navn.split()[0].lower() + navn.split()[1][0].lower()

# Teste funksjonen med eksempelnavnet
print(lagBrukernavn("Kari Nordmann"))

### OPPGAVE 2 ###

# Definere lagEpost() som tar inn brukernavn og e-post-hale
def lagEpost(brukernavn, suffix):
    return str(brukernavn).lower() + "@" + str(suffix).lower()

# Teste funksjonen med eget brukernavn og IFI-suffixet
print(lagEpost("jorgenao", "ifi.uio.no"))

### BONUS: OPPGAVE 5: Skrive tester for lagEpost() ###

def test_lagEpost():
    
    # Vanlig test-case
    resultat = lagEpost("jorgenao", "ifi.uio.no")
    forventet_resultat = "jorgenao@ifi.uio.no"
    assert resultat == forventet_resultat, "Forventet resultat var " + forventet_resultat + ", men funksjonen ga resultatet " + resultat
    
    # Border-case (store bokstaver)
    resultat = lagEpost("KARIN", "STUDENT.MATNAT.UIO.NO")
    forventet_resultat = "karin@student.matnat.uio.no"
    assert resultat == forventet_resultat, "Forventet resultat var " + forventet_resultat + ", men funksjonen ga resultatet " + resultat
    
    # Border-case (empty string)
    resultat = lagEpost("", "")
    forventet_resultat = "@"
    assert resultat == forventet_resultat, "Forventet resultat var " + forventet_resultat + ", men funksjonen ga resultatet " + resultat

test_lagEpost()

### OPPGAVE 3 ###

# Definere prosedyren med ordbok som argument
def skrivUtEposter(ordbok):
    for key in ordbok:
        print(lagEpost(key, ordbok[key]))

# Teste prosedyren med eksempelet fra oppgaveteksten
skrivUtEposter({"olan":"ifi.uio.no", "karin":"student.matnat.uio.no"})

### OPPGAVE 4 ###

# Lage en tom ordbok
bruker_ordbok = dict()

# Registrere første input fra brukeren
svar = input("Skriv 'i' for å legge inn navn, 'p' for å printe ut og 's' for å stoppe programmet: ")

# While-løkke for å la brukeren gjøre de ønskede operasjonene
while svar != "s":
    if svar == "i":
        navn = input("Skriv inn et navn: ")
        suffix = input("Skriv inn et e-postsuffix: ")
        brukernavn = lagBrukernavn(navn)
        bruker_ordbok[brukernavn] = suffix
    elif svar == "p":
        skrivUtEposter(bruker_ordbok)
    svar = input("Skriv inn neste kommando: ")

### BONUS: OPPGAVE 6 ###

# DENNE KODEN FUNKER, MEN JEG ORKET IKKE ENDRE RESTEN AV SCRIPTET
# UNCOMMENT DENNE BLOKKEN OG COMMENT RESTEN FOR Å TESTE BONUS-OPPGAVEN

# Funksjonen funker så lenge det ikke er for mange folk med samme navn, 
# altså så lenge i < len(etternavn). Har ikke gått videre og laget en løsning
# for dette. Men man kan f.eks. legge inn en test med if i > len(navn.split()[1])
# og deretter legge inn tall.

# def lagBrukernavn(navn, ordbok):  
    
#     assert len(navn.split()) == 2, 'Feil input! Du kan bare bruke fornavn og siste etternavn, adskilt med mellomrom. Eksempel: "Kari Nordmann".'
    
#     for letter in navn:
#         if letter.lower() == "æ":
#             i = navn.index(letter)
#             navn = navn[0:i] + "ae" + navn[i + 1: ]
#         elif letter.lower() == "ø":
#             i = navn.index(letter)
#             navn = navn[0:i] + "o" + navn[i + 1: ]
#         elif letter.lower() == "å":
#             i = navn.index(letter)
#             navn = navn[0:i] + "a" + navn[i + 1: ]
    
#     brukernavn = navn.split()[0].lower() + navn.split()[1][0].lower()
    
#     i = 1
    
#     while brukernavn in ordbok:
#         brukernavn = brukernavn + navn.split()[1][i].lower()
#         i += 1
    
#     return brukernavn

# # Legge inn to ordbøker for å teste
# ordbok1 = {"olan":"ifi.uio.no", "karin":"student.matnat.uio.no"}
# ordbok2 = {"olan":"ifi.uio.no", "karin":"student.matnat.uio.no", "olano":"ifi.uio.no"}

# # Teste utskriften fra funksjonen med begge ordbøkene
# print(lagBrukernavn("Ola Nordmann", ordbok1))
# print(lagBrukernavn("Ola Nordmann", ordbok2))
    
    