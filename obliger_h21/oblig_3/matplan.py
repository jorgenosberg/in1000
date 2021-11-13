'''
Oblig 3 | IN1000 | Høst 2021

Filnavn: matplan.py

KLAR FOR RETTING!

Dette programmet skal vise at jeg kan bruke en ordbok til å enkelt samle informasjon
om enkeltpersoner i en oversikt. 

Oppgave 4.3:

Hvilken type samling (liste, mengde, ordbok) ville du brukt for å representere hver av
de følgende eksemplene på data? Skriv litt om hvorfor, eventuelt med forbehold eller
presiseringer.

a. Brukernavn på alle IN1000 studentene
Hvis jeg kun ønsker en liste med alle brukernavn ville jeg ha brukt en vanlig Python-liste.
Hvis jeg ønsker å ha studentenes fulle navn som nøkkelverdi og matche navnet med brukernavnet, 
ville jeg ha brukt en ordbok.

b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
Her ville jeg ha brukt en ordbok for å enkelt matche brukernavn med resultat på innleveringen.
Da blir det lettere å hente ut kun brukernavn eller resultater, samt sjekke summen eller snittet
av innholdsverdiene (altså kun resultatet).

c. Alle vinnere i Lotto siste år (kun navn)
Hvis man her kun ønsker variabelen "lottovinnere" med en rekke variabler, kunne jeg ha vurdert å bruke en
mengde (array). Hvis det er veldig mange navn vil en NumPy-array være en mer effektiv måte å lagre dataen
på. NumPy-arrays krever mindre plass og mindre maskinkraft, og er derfor raskere å jobbe med. Men den største
fordelen med NumPy-arrays er at det er flere matematiske og vitenskapelige metoder man kan bruke direkte på
arrayen, f.eks. å dividere hele objektet. Fordi det her bare er snakk om noen navn, er det nok like greit med
en vanlig liste.

d. All mat noen gjester i et selskap er allergisk mot (for å planlegge menyen)
Jeg ville definitivt ha brukt en ordbok for å ha enkel tilgang på hver enkelt gjest og en liste over alle
allergier vedkommende eventuelt har. Omtrent akkurat som måltidsplanen i denne obligen.

'''

### OPPGAVE 4.1 ###

# Opprette ordboken med måltidslister for hver beboer
måltider = {
    "Wenche Ambjørnsrud": ["Knekkebrød", "ertesuppe", "taco"],
    "Anders Andersson": ["Cornflakes", "eggerøre og røkelaks", "indrefilet av svin"],
    "Magnhild Vatne": ["Brødskiver med syltetøy", "lapskaus", "Beef Wellington"]
}

### OPPGAVE 4.2 ###

# Lage en prosedyre for å skrive ut matplanen for en gitt beboer 
def checkMealPlan():
    for key in måltider:
        print(key)
    
    beboer = input("Skriv inn navnet på beboeren du ønsker å hente matplanen for: ").title()
    
    if beboer not in måltider:
        print("Navnet du oppga er dessverre ikke registrert på sykehjemmet.")
    else:
        print(f"{beboer} skal spise: ")
        print(*måltider[beboer], sep = ", ")

# Kalle prosedyren
checkMealPlan()