'''
Oblig 3 | IN1000 | Høst 2021

Filnavn: billettpris.py

KLAR FOR RETTING!

Dette programmet skal definere en prosedyre for å sjekke alderen på
en kjøper og kalkulere riktig alder. 

Programmet skal også vise at jeg forstår logikken og rekkefølgen i
en if-else-test.

'''

### OPPGAVE 3.1-3.4 ###

# Definere prosedyren for å sjekke og teste alder opp mot billettpris
def checkTicketPrice():
    
    alder = int(input("Hvor gammel er kjøperen? "))
    billettpris = 0
    
    if alder <= 17:
        billettpris = 30
        print(f"Kjøperen er 17 år eller yngre, og skal derfor betale {billettpris} kroner (barnebillett)")
    elif alder >= 63:
        billettpris = 35
        print(f"Kjøperen er 63 år eller eldre, og skal derfor betale {billettpris} kroner (honnørbillett)")
    else:
        billettpris = 50
        print(f"Kjøperen er over 17 år, og skal derfor betale {billettpris} kroner (voksenbillett)")

# Kjøre prosedyren
checkTicketPrice()

### OPPGAVE 3.5 ###

# Teste prosedyren med 15, 31 og 63
# checkTicketPrice()
# checkTicketPrice()
# checkTicketPrice()

# Jeg oppdaget problemet med rekkefølgen fra oppgaveteksten før jeg skrev inn if-else-testen, 
# og la derfor inn den riktige logikken. Special cases må sjekkes først, for alle pensjonister
# er jo også over 17.