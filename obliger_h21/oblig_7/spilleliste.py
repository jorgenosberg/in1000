'''
Oblig 7 | IN1000 | Høst 2021

Filnavn: spilleliste.py
Oppgave: 3

Denne filen svarer på oppgave 3 i oblig 7, og har som mål å opprette
en klasse Spilleliste som skal kunne brukes sammen med klassen Sang. 
Spillelisten skal ha et navn og en tom liste som kan fylles med Sang-
objekter, samt flere metoder for å bruke den.

__str__ skal returnere en lesbar streng med info om spillelisten, 
lesFraFil() skal lese en tekstfil og legge inn sangene som finnes i filen
i spillelisten.
leggTilSang() skal legge til en sang direkte, mens fjernSang() skal fjerne én.
I tillegg skal spillelisten ha en metode for å spille av både én sang eller
flere, samt to metoder for å finne en sang i spillelisten og hente ut 
flere sanger av én artist.
'''

from sang import Sang # Importerer den nye klassen Sang rett fra filen sang.py

class Spilleliste:
    def __init__(self, listenavn:str) -> None:
        self._sanger = list() # Oppretter en tom liste som kan fylles med sanger
        self._navn = listenavn

    def __str__(self) -> str: # Returnerer en lesbar streng
        return f"Spillelisten {self._navn}. Inneholder {len(self._sanger)} sanger."
    
    def lesFraFil(self, filnavn:str): # Åpner filen, itererer gjennom og legger til sanger, og lukker filen
        with open(filnavn) as fil:
            for linje in fil:
                deler = linje.strip().split(";")
                sang = Sang(deler[1], deler[0])
                self.leggTilSang(sang)
    
    def leggTilSang(self, nySang:Sang) -> None: 
        self._sanger.append(nySang)
    
    def fjernSang(self, sang:Sang) -> None:
        self._sanger.remove(sang)
    
    def spillSang(self, sang:Sang) -> None:
        sang.spill()
    
    def spillAlle(self) -> None: # Itererer gjennom listen og spiller av alle
        for sang in self._sanger:
            sang.spill()
    
    def finnSang(self, tittel:str) -> Sang or None: # Itererer gjennom listen og sjekker tittelen
        for sang in self._sanger:
            if sang.sjekkTittel(tittel) == True:
                return sang
        return None
    
    def hentArtistUtvalg(self, artistnavn:str): # Itererer gjennom listen og appender sanger til en ny liste utvalg
        utvalg = list()
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn) == True:
                utvalg.append(sang)
        return utvalg

