'''
Oblig 7 | IN1000 | Høst 2021

Filnavn: test_avspilling.py
Oppgave: 4 (frivillig utvidelse)

Dette programmet tester om Sang-klassen fra sang_utvidet.py funker som
den skal. Den følger instruksene i den frivillige utvidelsen
og oppretter altså en Spilleliste-instans som deretter spiller
av sangene i listen.

Den bruker play().wait_done() for å spille av, og man må derfor vente til
sangen er ferdig før programmet kjører neste kodelinje. 

Eventuelt kan man bruke Ctrl+C for å avbryte, og kun kjøre den med 1 sang
av gangen. Altså commente linje 27 og 32 og kjøre på nytt.

Med litt mer tid ville jeg nok ha prøvd meg på å lage en avspiller med litt
flere funksjoner, for eksempel med både play, pause og stop mens sangen blir
avspilt.
'''

from sang_utvidet import Sang
from spilleliste import Spilleliste

def hovedprogram():
    sang1 = Sang("Albinoni", "Adagio", "lydfiler/adagio.wav") # lagrer 
    sang2 = Sang("Beethoven", "Ode to Joy", "lydfiler/ode_to_joy.wav")
    
    spilleliste = Spilleliste("Test av lydfiler")
    
    spilleliste.leggTilSang(sang1)
    spilleliste.leggTilSang(sang2)
    
    spilleliste.spillAlle()

hovedprogram()