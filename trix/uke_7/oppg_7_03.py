'''
TRIX-OPPGAVE 7.03

I denne oppgaven skal vi modellere en kapselmaskin for espresso. 
Maskinen har to innstillinger, espresso (liten kopp) og lungo (større kopp). 
Maskinen kan ikke lage kaffe uten nok vann. En espresso krever 40ml, og en lungo krever 110ml. 
Maskinens vanntank er på 1000ml -- én liter.

Gitt grensesnittet under, programmer klassen EspressoMaskin. 
Du kommer til å måtte definere dine egne instansvariabler når du skal løse denne oppgaven, 
og du står også fritt til å definere egne metoder i klassen. 
Du kan la metodene skrive beskjeder til brukeren i termnalen.

Lag også et testprogram som simulerer en kaffemaskin ved å be om kommandoer 
og deretter kaller på passende metode (ikke med i løsningsforslaget).
'''

class EspressoMaskin:
    #Konstruktør
    def __init__(self, kapasitet):
        self._kapasitet = kapasitet
        self._vannmengde = 0

    # Lag espresso dersom det er nok vann
    def lagEspresso(self):
        if self._vannmengde >= 40:
            self._vannmengde -= 40
            print("Din espresso er klar!")
        else:
            print("Det er ikke nok vann til en espresso. Du må fylle på mer!")

    # Lag lungo dersom det er nok vann
    def lagLungo(self):
        if self._vannmengde >= 110:
            self._vannmengde -= 110
            print("Din lungo er klar!")
        else:
            print("Det er ikke nok vann til en lungo. Du må fylle på mer!")

    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyllVann(self, ml):
        if (self._vannmengde + ml) <= self._kapasitet:
            self._vannmengde += ml
            print(f"Du fylte {ml} ml. Det er nå {self._vannmengde} ml på vanntanken.")
        else:
            print(f"Du kan ikke fylle så mye. Fylte bare {self._kapasitet - self._vannmengde} ml, slik at det nå er {self._kapasitet} ml på vanntanken.")
            self._vannmengde = self._kapasitet
            
    # Les av tilgjengelig vann i ml
    def hentVannmengde(self):
        return self._vannmengde




