'''
Oblig 7 | IN1000 | Høst 2021

Filnavn: sang_utvidet.py
Oppgave: 4

Denne filen svarer på oppgave 4 i oblig 7, som er en frivillig utvidelse
som faktisk skal la oss spille av lydfiler på maskinen vår gjennom Python.

Programmet importerer biblioteket simpleaudio og bruker dette for å
lage en utvidet Sang-klasse som inneholder metoder for å spille av filene.

Fordi sangtester.py ikke forutsetter at Sang-klassen har filnavn som
instansvariabel, lager jeg denne klassen i en egen fil. 

Den testes også i test_avspilling.py.

Oppgaven ber oss om å bruke play().wait_done() for å spille av sangen, som
betyr at den ikke stopper før den er ferdig. Her må man enten vente eller
bare bruke Ctrl+C for å avbryte kjøringen.
'''

import simpleaudio

class Sang:
    def __init__(self, artist:str, tittel:str, filnavn:str) -> None:
        self._tittel = tittel
        self._artist = artist
        self._filnavn = filnavn # Legger til filnavn ved opprettelsen av instansen
    
    def __str__(self) -> str:
        return f"«{self._tittel}» av {self._artist}"
    
    def __repr__(self) -> str:
        return f"«{self._tittel}» av {self._artist}"
    
    def spill(self) -> None: # Bruker simpleaudio-funksjoner for å spille av lydfilen med riktig filnavn
        print(f"Spiller {str(self)}")
        lydfil = simpleaudio.WaveObject.from_wave_file(self._filnavn)
        play_lydfil = lydfil.play()
        play_lydfil.wait_done()
    
    def sjekkArtist(self, artist:str) -> bool:
        if any(navn in self._artist.lower().split() for navn in artist.lower().split()): # Sjekker om ett eller flere navn i tekststrengen finnes i instansvariabelen
            return True
        else:
            return False
    
    def sjekkTittel(self, tittel:str) -> bool:
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False
    
    def sjekkArtistOgTittel(self, artist:str, tittel:str) -> bool:
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel) == True:
            return True
        else:
            return False