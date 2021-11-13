'''
Oblig 8 | IN1000 | Høst 2021

Filnavn: hovedprogram.py
Oppgave: 5

Denne filen svarer på oppgave 5 i oblig 8, og inneholder et hovedprogram()
som skal teste at Datasenter-klassen og alle tilhørende klasser fungerer
som de skal.

Hovedprogrammet skal opprette én instans av Datasenter og to instanser av
Regneklynge vha. de to filene "saga.txt" og "abel.txt". Deretter skal programmet
iterere gjennom de to regneklyngene og skrive ut viktig informasjon om begge.
'''

from datasenter import Datasenter

# Definerer et hovedprogram() for å teste Datasenter-klassen og alle tilhørende klasser
def hovedprogram():
    # Oppretter en instans av klassen Datasenter med plass til to regneklynger
    # USIT = Universitetets senter for informasjonsteknologi 
    usit = Datasenter("USIT", 2)

    # Bruker prosedyremetoden lesInnRegneklynge() fra Datasenter for å lese inn
    # all informasjonen om Saga og Abel
    usit.lesInnRegneklynge("saga.txt")
    usit.lesInnRegneklynge("abel.txt")

    # Printer en ryddig overskrift
    print(f"\nDatasenteret {usit.getNavn()} har {len(usit.getRegneklynger())} regneklynger:\n")
    
    # Definerer en "counter" til for-loopen
    i = 1
    
    # Itererer gjennom de to regneklyngene og skriver ut all informasjonen om begge to
    for regneklynge in usit.getRegneklynger().values():
        
        print(f"### {i} ###\n") # printer header med counter
        
        print(f"-- Regneklyngen {regneklynge.getNavn()} --") # printer navnet
        print(f"Antall racks: {regneklynge.antRacks()}") # printer antall racks
        print(f"Antall prosessorer: {regneklynge.antProsessorer()}") # printer antall prosessorer
        
        minnekapasitet = regneklynge.getTotMinne() # lagrer total minnekapasitet for å sjekke størrelse
        
        if len(str(minnekapasitet)) > 3: # hvis kapasiteten tilsvarer terabytes:
            print(f"Total minnekapasitet: {round(minnekapasitet/1000)} TB")
        else: # hvis kapasiteten tilsvarer gigabytes:
            print(f"Total minnekapasitet: {minnekapasitet} GB")
            
        print(f"Noder med minst 32 GB: {regneklynge.noderMedNokMinne(32)}") # printer antall noder med minst 32 GB
        print(f"Noder med minst 64 GB: {regneklynge.noderMedNokMinne(64)}") # printer antall med minst 64 GB
        print(f"Noder med minst 128 GB: {regneklynge.noderMedNokMinne(128)}\n") # printer antall med minst 128 GB
        
        i += 1 # øker counteren

# Kjører testprogrammet
hovedprogram()