'''
Oblig 8 | IN1000 | Høst 2021

Filnavn: datasenter.py
Oppgave: 2 og 5

Denne filen svarer på oppgave 2 og 5 i oblig 8, og inneholder klassedefinisjonen
med grensesnitt og implementasjon for klassen Datasenter.

Klassen skal kunne holde styr på flere instanser av klassen Regneklynge og må
inneholde metoder som kan legge inn/lese inn regneklynger og skrive ut litt informasjon
om Datasenteret.
'''

from node import Node
# from rack import Rack
from regneklynge import Regneklynge

# Definerer klassen Datasenter for å holde styr på flere Regneklynger
class Datasenter:
    
    # Konstruktør som tar inn maks regneklynger
    #   @param navn = navn på datasenteret
    #   @param maksRegneklynger = antall regneklynger datasenteret har plass til
    #   @instansvariabel _regneklynger = ordbok der alle regneklyngene
    #   @return None
    def __init__(self, navn:str, maksRegneklynger:int) -> None:
        self._navn = navn
        self._maksRegneklynger = maksRegneklynger
        self._regneklynger = dict()
    
    # Definerer en representasjons-metode som gir en lettlest beskrivelse av instansen
    #   @param ingen parametre
    #   @return string med info om datasenteret
    def __repr__(self) -> str:
        return f"Datasenteret {self._navn}. Inneholder {len(self.getRegneklynger())} regneklynger: {self.getRegneklynger()}"
    
    # Definerer en string-metode som gir samme beskrivelse dersom man kaller på str(instans)
    #   @param ingen parametre
    #   @return string med info om datasenteret
    def __str__(self) -> str:
        return f"Datasenteret {self._navn}. Inneholder {len(self.getRegneklynger())} regneklynger: {self.getRegneklynger()}"
    
    # En getter som henter navnet på datasenteret
    #   @param ingen parametre
    #   @return self._navn
    def getNavn(self) -> str:
        return self._navn
    
    # En getter som henter ordboken med regneklynger
    #   @param ingen parametre
    #   @return self._regneklynger (type: dict())
    def getRegneklynger(self) -> dict:
        return self._regneklynger
    
    # Prosedyremetode for å lese inn informasjon om en regneklynge fra en fil, opprette en instans
    # og legge den inn i ordboken self._regneklynger
    #   @param filnavn = filen som skal leses
    #   @return None
    def lesInnRegneklynge(self, filnavn) -> None:
        
        # Lager en variabel navn fra filnavnet
        navn = filnavn.removesuffix(".txt").capitalize()

        # Åpner, leser og lukker filen
        with open(filnavn) as fil: # åpner filen
            
            linjer = list() # tom liste hvor jeg skal ha linjene i filen
            
            for linje in fil:
                linjer.append(linje) # legger inn hver linje
            
            noderPerRack = int(linjer[0]) # oppretter en variabel fra første indeks
                
            # Legger inn den nye regneklyngen vha. navn og noderPerRack
            self._regneklynger[navn] = Regneklynge(navn, noderPerRack)
            
            for linje in linjer[1:]:
                deler = linje.split() # splitter innholdet ved mellomrom og returnerer en liste
                
                node = Node(int(deler[1]), int(deler[2])) # oppretter en Node med informasjon fra andre linje
                
                # Setter inn det oppgitte antallet noder av eksempelnoden fra linjen
                for x in range(int(deler[0])):
                    self._regneklynger[navn].settInnNode(node)
    
    ### EKSTRA METODER ###
    
    # Prosedyremetode for å sette inn en instans av Regneklynge som allerede er opprettet
    #   @param navn på regneklyngen, vil bli nøkkel i ordboken
    #   @param selve regneklyngen, vil bli innholdsverdi i ordboken
    #   @return None 
    def settInnRegneklynge(self, navn, regneklynge) -> None:
        self._regneklynger[navn] = regneklynge
    
    # Funksjonsmetode for å regne ut total minnekapasitet i hele datasenteret
    #   @param ingen parametre
    #   @return total minnekapasitet som int
    def getTotMinne(self) -> int:
        return sum([regneklynge.getTotMinne() for regneklynge in self._regneklynger])