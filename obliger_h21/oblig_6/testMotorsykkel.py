'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: testMotorsykkel.py

KLAR FOR RETTING!

Dette programmet skal teste klassen Motorsykkel fra "motorsykkel.py".
Koden skal inneholde et hovedprogram() som oppretter flere "motorsykler", 
altså ulike av klassen. Deretter skal den skrive ut informasjon om motorsyklene
og kalle på noen av metodene som er inkludert i klasse-definisjonen.

'''

### OPPGAVE 1.5

# Importerer klassen direkte fra filen motorsykkel.py
from motorsykkel import Motorsykkel

### OPPGAVE 1.5-1.7 ###

# Definerer en enkel prosedyre for å løse deloppgavene 5-7
def hovedprogram():
    # Opprette de nye instansene av Motorsykkel-klassen
    honda = Motorsykkel("Honda", "AY6949", 4900)
    kawasaki = Motorsykkel("Kawasaki", "BT4127", 2150)
    harley = Motorsykkel("Harley Davidson", "FN5505", 12000)
    
    # Skrive ut alle attributes for hver instans
    # Foretrekker å gjøre det enkelt og penere med en for-loop, så jeg lagrer instansene i en liste
    liste = [honda, kawasaki, harley]
    for motorsykkel in liste:
        print(f"\nMotorsykkel nr. {(liste.index(motorsykkel)+1)}:")
        motorsykkel.skrivUt()
    
    # Øke kilometerstanden på den siste motorsykkelen
    harley.kjor(10)

    # Sjekke den nye kilometerstanden
    print(f"\nDen nye kilometerstanden for Harley-motorsykkelen er: {harley.hentKilometerstand()} km.")

### OPPGAVE 1.8 ###

# Kalle på prosedyren hovedprogram() for å teste klassen og metodene
hovedprogram()