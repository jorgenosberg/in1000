'''
Oblig 2 | IN1000 | Høst 2021

Filnavn: kodeforstaaelse.py

Dette programmet svarer på oppgave 4 i Oblig 2.
Målet er å kunne vurdere en kodeblokk og se om koden er "lovlig".

Teorispørsmålene fra oppgaveteksten:
1. Er dette lovlig kode? Begrunn svaret.

Første og andre linje er unødvendig kompliserte, men for så vidt lovlige
i Python. Språket leser input() som string, derfor må man bruke int()
for å lese heltallet. Dette kunne imidlertid ha vært gjort enklere - vha.
int(input("Tast inn et heltall! ")).

Det som derimot ikke er mulig i Python, er concatenation mellom
int() og string(). Dermed vil ikke print(b + "Hei!") kjøre. Her kan man
enten bruke en formatert string: print(f"{b} Hei!") eller gjøre om
variabelen b til string når man printer: print(str(b) + "Hei!").

2. Hvilke problemer vil vi kunne møte på når vi kjører denne koden?

Se svaret over. Python godtar ikke concatenation med både int() og string()
og vil derfor ikke kunne printe b + "Hei!" hvis tallet brukeren taster inn er
lavere enn 10.

Programmet tar heller ikke hensyn til hva brukerens input kan komme til å være.
Dersom brukeren taster inn bokstaver, vil ikke variabelen b bli definert. 
Dette er fordi int() ikke kan gjøre om en bokstavrekke til heltall.
'''

# Teste koden fra opppgaven selv
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + " Hei!")