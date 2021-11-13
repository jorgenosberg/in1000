'''
Oblig 8 | IN1000 | Høst 2021

Filnavn: regneklynge.py
Oppgave: 2

Denne filen svarer på oppgave 2 og 5 i oblig 8, og inneholder klassedefinisjonen
med grensesnitt og implementasjon for klassen Datasenter.

Klassen skal kunne holde styr på flere instanser av klassen Regneklynge og må
inneholde metoder som kan sjekke detaljer og egenskaper og 

Basert på grensesnittet som er oppgitt i grensesnitt.py og utvidet i henhold til
oppgaven.
'''

from node import Node
from rack import Rack

# Klasse for representasjon av regneklynge med racks og noder
class Regneklynge:
    
    # Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack
    #   @param noderPerRack max antall noder som kan plasseres i et rack
    def __init__(self, navn, noderPerRack:int) -> None:
        self._navn = navn
        self._noderPerRack = noderPerRack
        self._racks = list()

    # Funksjonsmetode for å gi en lettlest representasjon av objektet Regneklynge
    #   @param  ingen parametre
    #   @return string med info om regneklyngen
    def __repr__(self) -> str:
        return f"Regneklyngen {self.getNavn()}: {self.antRacks()} racks med {self.getTotMinne()} GB minne og {self.antProsessorer()} prosessorer."
    
    # Funksjonsmetode for å gi en lettlest string med info om objektet Regneklynge
    # når man kaller på str(instans)
    #   @param  ingen parametre
    #   @return string med info om regneklyngen
    def __str__(self) -> str:
        return f"Regneklyngen {self.getNavn()}: {self.antRacks()} racks med {self.getTotMinne()} GB minne og {self.antProsessorer()} prosessorer."
        
    # Getter for å hente ut instansvariabelen navn
    #   @param ingen parametre
    #   @return self._navn som string
    def getNavn(self) -> str:
        return self._navn
    
    # Plasserer en node inn i et rack med ledig plass, eller i et nytt
    #   @param node referanse til noden som skal settes inn i datastrukturen
    #   @return  None
    def settInnNode(self, node:Node) -> None:
        for rack in self._racks: # løkke gjennom alle racks
            if rack.getAntNoder() < self._noderPerRack:
                rack.settInn(node) # hvis det er plass, sett inn noden
                return
        self._nyttRack() # hvis det er fullt, bruk privat metode for å opprette et nytt tomt rack
        self._racks[-1].settInn(node) # sett inn noden i det siste racket i listen
        return
    
    # Beregner totalt antall prosessorer i hele regneklyngen
    #   @return totalt antall prosessorer
    def antProsessorer(self) -> int:
        return sum([rack.antProsessorer() for rack in self._racks])

    # Beregner antall noder i regneklyngen med minne over angitt grense
    #   @param paakrevdMinne hvor mye minne skal noder som telles med ha
    #   @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        totAnt = 0
        for rack in self._racks: # sjekk hvert rack i self._racks
            totAnt += rack.noderMedNokMinne(paakrevdMinne) # lagre ant noder med nok minne
        return totAnt
                
    # Henter antall racks i regneklyngen
    #   @param ingen parametre
    #   @return antall racks
    def antRacks(self) -> int:
        return len(self._racks)
    
    ### EKSTRA METODER ###
    
    # Prosedyremetode for å sette inn noder OG skrive ut info om hvor noden ble plassert
    #   @param node = instansen av Node som skal settes inn
    #   @return None
    def settInnMedPrint(self, node:Node) -> None:
        for rack in self._racks:
            if rack.getAntNoder() < self._noderPerRack:
                rack.settInn(node)
                print(f"Ny node ble satt inn i rack #{self._racks.index(rack)}.")
                return
        self._nyttRack()
        self._racks[-1].settInn(node)
        print(f"Det var ikke plass til noden i eksisterende racks. Noden ble satt inn i et nytt rack (#{len(self._racks)-1}).")
        return
    
    # Funksjonsmetode for å returnere total minnekapasitet i hele regneklyngen
    #   @param ingen parametre
    #   @return summen av getTotMinne() for alle racks
    def getTotMinne(self) -> int:
        return sum([rack.getTotMinne() for rack in self._racks])
    
    # Privat prosedyremetode for å sette inn nytt rack i regneklyngen
    #   @param  ingen parametre
    #   @return None          
    def _nyttRack(self) -> None:
        self._racks.append(Rack())