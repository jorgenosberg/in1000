'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: hund.py

Dette programmet skal bygge klassen Hund med en rekke ulike metoder.
Klassen skal inneholde en metode for instansvariabler, en metode for å
hente ut alder og vekt, samt to metoder for å springe/spise som også
modifiserer variablene vekt og metthet.

Filen inneholder kun klassen, ikke testen. Testen utføres i testHund.py.

KLAR FOR RETTING!

'''

# Definere klassen Hund med __init__-metoden for instansvariablene
class Hund:
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10 # Harcoder instansvariabelen _metthet som begynner på 10 for alle hunder
    
    # Definerer __repr__ for ordens skyld, slik at print(instans) viser nyttig informasjon (naturligvis en tegning av hunden)
    def __repr__(self):
        return f"en {self._alder} år gammel (og veldig søt) hund:\n\n   / \__\n  (    @\___\n  /         O\n /   (_____/\n/_____/"
    
    # Metoden hentAlder returnerer instansvariabelen _alder
    def hentAlder(self):
        return self._alder
    
    # Metoden hentVekt returnerer variabelen vekt
    def hentVekt(self):
        return self._vekt
    
    # Metoden spring trekker fra 1 fra _metthet pga. aktivitet, og 
    # reduserer _vekt med 1 dersom _metthet er under 5
    def spring(self):
        self._metthet =- 1
        if self._metthet > 5:
            self._vekt =- 1
    
    # Metoden spis øker mettheten med et gitt heltall, og øker
    # vekten dersom _metthet er over 7
    def spis(self, heltall):
        self._metthet += heltall
        if self._metthet > 7:
            self._vekt += 1