'''
Oblig 7 | IN1000 | Høst 2021

Filnavn: sang.py
Oppgave: 2

Denne filen svarer på oppgave 2 i 7. oblig, og inneholder kode som
oppretter en klasse ved navn Sang og definerer de ulike metodene
oppgaven spør etter.

Klassen skal lagre artist og tittel på én og én sang som instansvariabler, 
og må inneholde metoder både for å spille av en sang og vise en lesbar
representasjon av Self, og metoder for å sjekke om en sang har en spesifikk
tittel og/eller er av en spesifikk artist.
'''

class Sang: # Definerer klassen
    def __init__(self, artist:str, tittel:str) -> None: # Presiserer at __init__ ikke skal returne noe.
        self._tittel = tittel # Lagrer tittel
        self._artist = artist # Lagrer artist
    
    def __str__(self) -> str: # Definerer en __str__-metode for å gjøre str(self) lettere å lese
        return f"«{self._tittel}» av {self._artist}"
    
    def __repr__(self) -> str: # Gjør det samme med __repr__ i tilfelle man ikke bruker str(), men f.eks. bare print(self)
        return f"«{self._tittel}» av {self._artist}"
    
    def spill(self) -> None: # Definerer prosedyremetoden spill() som ikke returnerer noe
        print(f"Spiller {str(self)}") # Jeg printer ut hva som blir spilt av
    
    def sjekkArtist(self, artist:str) -> bool: # Definerer funksjonsmetoden sjekkArtist()
        if any(navn in self._artist.lower().split() for navn in artist.lower().split()): # Sjekker om ett eller flere navn i tekststrengen finnes i instansvariabelen
            return True
        else:
            return False
    
    def sjekkTittel(self, tittel:str) -> bool: # Gjør det samme med tittel, men her må de være prikk like
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False
    
    def sjekkArtistOgTittel(self, artist:str, tittel:str) -> bool: # Sjekker både artist og tittel vha. de andre funksjonene
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel) == True:
            return True
        else:
            return False