'''
Oblig 8 | IN1000 | Høst 2021

Filnavn: node.py
Oppgave: 2

Denne filen svarer på oppgave 2 i oblig 8, og inneholder klassedefinisjonen
med grensesnitt og implementasjon for klassen Node.

Hver instans av klassen skal representere én Node i et rack som igjen er en
del av en regneklynge. Noden er en datamaskin, og må inneholde variabler blant
annet for minne (RAM) og antall prosessorer (CPU). 

Klassen må tilby metoder som henter minne og antall prosessorer (gettere), 
samt en metode for å sjekke om noden har nok minne til et gitt program.

Basert på grensesnittet som er oppgitt i grensesnitt.py og utvidet i henhold til
oppgaven.
'''

# Klassedefinisjonen for noder i rack i regneklynge
class Node:
    
    # Oppretter en node med gitt minne-storrelse og antall prosessorer
    #   @param minne = GB minne i den nye noden
    #   @param antPros = antall prosessorer i den nye noden
    #   @return None
    def __init__(self, minne, antProsessorer) -> None:
        self._minne = minne
        self._antProsessorer = antProsessorer
    
    # Definerer en representasjons-metode som gir en lesbar streng når instansen kalles
    #   @param ingen parametre
    #   @return string med ryddig info om instansen
    def __repr__(self) -> str:
        return f"Node med {self.getMinne()} GB minne og {self.antProsessorer()} prosessorer."

    # Definerer en str-metode som gjør det samme som __repr__ dersom str(instans) blir kalt
    #   @param ingen parametre
    #   @return string med ryddig info om instansen
    def __str__(self) -> str:
        return f"Node med {self.getMinne()} GB minne og {self.antProsessorer()} prosessorer."
        
    # Henter antall prosessorer i noden
    #   @param ingen parametre
    #   @return antall prosessorer i noden
    def antProsessorer(self) -> int:
        return self._antProsessorer
    
    # Getter som returnerer instansvariabelen _minne
    #   @param ingen parametre
    #   @return self._minne som int
    def getMinne(self) -> int:
        return self._minne

    # Sjekker om noden har tilstrekkelig minne for et program
    #   @param paakrevdMinne = GB minne som kreves for programmet
    #   @return bool, True hvis noden har minst saa mye minne
    def nokMinne(self, paakrevdMinne: int) -> bool:
        if paakrevdMinne <= self._minne:
            return True
        else:
            return False
    
    ### EKSTRA METODER ###
    
    # Definerer en prosedyremetode, type setter, som tillater
    # oppgradering av minnet i noden uten å opprette en ny
    #   @param minne = mengden minne som skal settes inn
    #   @return None
    def oppgraderMinne(self, minne) -> None:
        self._minne += minne
    
    # Definerer en prosedyremetode, type setter, som øker
    # antall prosessorer i noden uten å opprette en ny
    #   @param antall = antall prosessorer som skal settes inn
    #   @return None
    def oppgraderPros(self, antall) -> None:
        self._antProsessorer += antall
        
    # En samlet prosedyremetode som tillater oppgradering av
    # både minne og prosessorer på en gang
    #   @param minne = mengden minne
    #   @param antPros = antall prosessorer som skal legges til
    #   @return None
    def oppgraderNode(self, minne, antPros) -> None:
        self._minne += minne
        self._antProsessorer += antPros