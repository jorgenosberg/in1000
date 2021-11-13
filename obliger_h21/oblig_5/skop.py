'''
Oblig 5 | IN1000 | Høst 2021

Filnavn: skop.py

KLAR FOR RETTING!

I denne filen skal jeg forsøke å forklare hvordan koden fra
oppgave 3 (skop) faktisk kjører i Python. 

Jeg vil først prøve å forklare det med ord, deretter visualisere det
med kommentarer direkte i koden, og til slutt vil jeg teste koden her
i Python og se hvordan den faktisk blir kjørt.

Beskrivelse med ord:
Først definerer programmet funksjonen minFunksjon() som ikke tar imot
noen parametre, men som har en returverdi(b). Deretter defineres prosedyren
hovedprogram(), også denne uten parametre. Inne i prosedyren hovedprogram()
kalles også funksjonen minFunksjon(), men dette vil ikke skje før hovedprogram()
faktisk blir kalt. Til slutt kalles hovedprogram() og Python begynner dermed å
kjøre hovedprogram()-prosedyren fra øverste linje. 

Når hovedprogram() kjører blir først variabelen a = 42 definert, deretter b = 0.
Så printes b til terminalen, og det som skrives ut er altså 0. Deretter defineres
b = a, og verdien til b er nå lik verdien til a, altså 42. Så prøver hovedprogram()
å definere a som returverdien til funksjonen minFunksjon() – dermed kjøres funksjonen
minFunksjon().

Inne i minFunksjon() starter en for-løkke som skal gå to ganger, altså så lenge
den er innenfor range(2). Først defineres c = 2 og printes til terminalen. Deretter
øker verdien av c med 1 i c += 1. Deretter defineres b = 10. Her går det imidlertid
galt. Når minFunksjon() prøver å oppdatere verdien til b og legge til verdien av
a, refererer a kun til en variabel som er definert inne i hovedprogram(), ikke i 
scriptet generelt. Derfor vil Python få en error av typen "name 'a' is not defined"
eller lignende.

Prosedyren hovedprogram() stopper altså på fjerde linje, og funksjonen minFunksjon()
stopper på sjette linje. Verdiene 0 og 2 blir printet til terminalen før feilmeldingen, 
men ikke noe annet blir skrevet ut.
'''

def minFunksjon(): # Definerer minFunksjon, kjøres ikke ennå
    for x in range(2): # sjette linje
        c = 2 # syvende linje
        print(c) # åttende linje, printer 2 til terminal
        c += 1 # niende linje
        b = 10 # tiende linje
        b += a # ellevte linje, error fordi a ikke er definert, funksjonene stopper
        print(b) # KJØRER IKKE
    return(b) # KJØRER IKKE

def hovedprogram(): # Definerer hovedprogram(), kjøres ikke ennå
    a = 42 # andre linje
    b = 0 # tredje linje
    print(b) # fjerde linje, printer 0 til terminal
    a = minFunksjon() # femte linje
    print (b) # KJØRER IKKE
    print (a) # KJØRER IKKE

hovedprogram() # Første linje som kjøres i programmet