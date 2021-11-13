'''
Oblig 5 | IN1000 | Høst 2021

Filnavn: oppgave_5.py

KLAR FOR RETTING!

Dette programmet svarer på den foreslåtte utfordringen i 
oppgave 5 i obligen.

Programmet skal lese inn informasjon fra en fil jeg oppretter
som inneholder størrelsesmål i tommer og deretter bruke funksjonen 
tommerTilCm() fra en tidligere oppgave for å skrive ut målene i cm. 
'''

### OPPGAVE 5.1 og 5.2 ###

# Kode for å lage en ny .txt-fil med informasjonen fra oppg-teksten
fil = open("mål_oppg_5.txt", "w")
fil.write("Skulderbredde 4\nHalsvidde 3.2\nLivvidde 10")
fil.close()

# Åpne filen og lagre informasjonen i en ordbok
ordbok = dict() # tom ordbok
for linje in open("mål_oppg_5.txt"):
    ordbok[str(linje.split()[0])] = float(linje.split()[1]) # bruker .split()-for å skille ved mellomrom

# Tester at ordboken ble riktig ved å printe
print(ordbok)

# Importere tommerTilCm()-funksjonen fra "regnefunksjoner.py"
from regnefunksjoner import tommerTilCm
 
# Skrive ut målene fra ordboken i centimeter
for key in ordbok:
    print(f"Målet for {key.lower()} ({ordbok[key]}) tilsvarer {tommerTilCm(ordbok[key])} centimeter.")