'''
Oblig 4 | IN1000 | Høst 2021

Filnavn: oppgave_5.py

KLAR FOR RETTING!

Dette programmet skal bruke while-løkker og lister for å lage en irriterende og
frustrerende gjettelek.

Ordene eller tallene brukeren skal gjette på må lagres i en egen liste, 
og du skal bruke en while-løkke for å utføre operasjoner frem til brukeren
taster et av de riktige svarene.

Lykke til!
'''
# Importere randint fra random-biblioteketer
from random import randint

# Lage en liste med "hemmelige ord" som er IFI-relatert
hemmelige_ord = ["Python", "UiO", "IFI"]

# Lage en liste med kjipe kommentarer som kan skrives ut når brukeren taster feil
kjipe_kommentarer = ["Du suger! Kanskje på tide å ta kvelden? Neida, prøv igjen!", 
                     "Dette var skuffende. Prøv igjen!", 
                     "Ahh, det er visst feil! Prøv igjen! You can do it!", 
                     "WRONG, BITCH! TRY AGAIN!", 
                     "Aiaiai. Den svir! Et forsøk til!", 
                     "Dårlig stil, ass. Prøv igjen!", 
                     "HAHAHAHAHA. Kanskje du skal prøve igjen?",
                     "Det er egentlig litt overraskende at du kom deg gjennom ungdomsskolen."
                     ]

# Definere en variabel for antall gjetninger brukeren bruker
antall_gjetninger = 0

# Fortelle brukeren hva som er målet og hente første svar
print(f"Velkommen til Jørgens gjettelek!\nDu skal nå prøve å gjette ett av tre hemmelige ord jeg har lagt inn i listen min.")
print("Du trenger bare å gjette ett av de tre ordene for å vinne!")
print("Hint: Alle ordene har med informatikk-studiet å gjøre.")
svar = input("Prøv å gjette det hemmelige ordet: ")

# Jeg bruker (len(liste)-1) i randint() for å sikre at 
# de kjipe kommentarene ikke kommer flere ganger enn én.
while svar not in hemmelige_ord:
    antall_gjetninger += 1
    if (len(kjipe_kommentarer)-1) > 0:
        i = randint(0, (len(kjipe_kommentarer)-1))
        print(kjipe_kommentarer[i])
        kjipe_kommentarer.pop(i)
    else:
        print("Det er fortsatt feil. Prøv igjen!")
    svar = input("Prøv å gjette det hemmelige ordet: ")

# Fortelle brukeren at det var riktig og hvor mange forsøk hen brukte
print(f"\nHurra for Norge!\nDu brukte {antall_gjetninger} forsøk.")

# Legge inn en spydig kommentar for de som bruker ekstreeeeemt lang tid.
if antall_gjetninger > 8:
    print("På den tiden du brukte på å komme frem til rett svar, kunne vi ha løst klimakrisen. Tygg litt på den!")

# Takke for i dag!
print("Takk for i dag! Prekæs!")