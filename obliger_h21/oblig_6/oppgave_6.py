'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: oppgave_6.py

KLAR FOR RETTING!

I denne oppgaven prøver jeg å bruke flere klasser for å simulere
en runde med kortspillet Krig.

Vanligvis ville jeg ha laget 1 fil per klasse, men for at du skal kunne lese og
kjøre alt i en fil har jeg inkludert det her.

OBS: Koden for å kjøre spillet er commented

Reglene er enkle – to spiller trekker ett og ett kort hver. Spilleren
kortet med høyest verdi vinner første trekning. Hvis kortene er like, 
blir det krig. Da må begge spillere legge 3 kort hver med forsiden ned, 
og deretter trekke et nytt kort. Den som får kortet med høyest verdi
vinner "stikket". Målet er å sitte igjen med alle kortene.

PROBLEM: Denne utgaven av krig går bare til kortstokken er tom - ikke
til én spiller sitter igjen med hele. Det er jo det som er de vanlige 
reglene. 
Det kunne ha vært løst ved å alltid lagre kortene spilleren vinner i en
egen bunke spilleren kan spille videre med. Da kunne spillet ha fortsatt 
helt til én av spillerne har 0 kort eller 52 kort, avhengig av hvordan
man bygger opp logikken.

Men jeg tenkte det holdt å lage en enkel 1v1-sim denne gangen. 

KILDE: Jeg har hentet inspirasjon til strukturen på kortstokken fra Colt Steeles
Modern Python 3 Bootcamp, der han har en deck_of_cards-øvelse med klasser. Det er særlig
nøstet for-løkke assigning av kort jeg fikk bruk for.
'''
from random import shuffle

class Kort:
	def __init__(self, farge, verdi): # Henter verdi og farge fra Kortstokk-klassen når den opprettes
		self.farge = farge
		self.verdi = verdi
		self.tallverdi = self.get_tallverdi() # Lagrer tallverdien som 

	def __repr__(self): # Returnerer verdi og farge på kortet som en streng. Eks: "Hjerter 10"
		return f"{self.farge} {self.verdi}"

	def get_tallverdi(self):
		verdier = ["2","3","4","5","6","7","8","9","10","Knekt","Dronning","Konge", "Ess"]
		return verdier.index(self.verdi)+2 # Returnerer tallverdien av hvert kort, 2 = 2 og Ess = 14

class Kortstokk:
	def __init__(self):
		farger = ["Hjerter", "Ruter", "Kløver", "Spar"]
		verdier = ["2","3","4","5","6","7","8","9","10","Knekt","Dronning","Konge", "Ess"]
		self.kort = [Kort(farge, verdi) for farge in farger for verdi in verdier]

	def __repr__(self): # Returnerer en streng som forteller hva kortstokken er (med antall kort)
		return f"En kortstokk med {self.tell_kort()} kort"

	def tell_kort(self): # Teller antall kort i kortstokken
		return len(self.kort)

	def stokke(self): # Bruker shuffle fra random-biblioteket for å stokke kortstokken
		if self.tell_kort() < 52: # Sjekker at kortstokken
			raise ValueError("Kun hele kortstokker (52 kort) kan bli stokket.")
		shuffle(self.kort)
		return self

	def _dele_ut(self, antall): # Denne er private, men brukes i dele_ut_kort og dele_ut_hånd
		count = self.tell_kort()
		# Sjekker hva som er minst av antall og rest. kort og bestemmer maks kort som kan deles ut
		maks = min([count, antall]) 
		if count == 0: # Sjekker om det er flere kort igjen, gir error hvis kortstokken er tom
			raise ValueError("Alle kortene har blitt delt ut.")
		kort = self.kort[-maks:] # Indekserer fra maks antall kort og lagrer dem
		self.kort = self.kort[:-maks] # Oppdaterer self.kort og fjerner kortene som har blitt delt ut
		return kort # Returnerer kortene som blir delt ut som en liste

	def dele_ut_kort(self):
		return self._dele_ut(1)[0] # Deler ut 1 kort fra "toppen" av bunken

	def dele_ut_hånd(self, antall):
		return self._dele_ut(antall) # Deler ut et "stikk", et gitt antall kort

class Spiller: # Oppretter en Spiller slik at jeg kan lagre seiere og navn på en ryddig måte
    def __init__(self, navn):
        self.navn = navn
        self.seiere = 0
        self.kort = None
    
    def øk_seier(self): # Legger til en metode som øker seier-counten med 1 for hver seier
        self.seiere += 1
    
    def get_seiere(self): # Returnerer tallverdien 
        return self.seiere
        
class Krig:
    def __init__(self): # Lagrer spillerne og kortstokken som attributes
        self.spiller1 = Spiller(input("Navn på spiller 1: "))
        self.spiller2 = Spiller(input("Navn på spiller 2: "))
        self.kortstokk = Kortstokk().stokke()

    def seiere(self, vinner): # Sjekker og skriver ut vinneren av hver runde
        if vinner == self.spiller1.navn:
            self.spiller1.øk_seier() # Øker seier-instansvariabelen for spiller1
        else:
            self.spiller2.øk_seier() # Samme for spiller2
        print(f"{vinner} vinner denne runden!\n")

    def print_kort(self, spiller1, kort1, spiller2, kort2): # Skriver ut hvilke kort spillerne har trukket (og tallverdi)
        print(f"\n{spiller1} trakk: {kort1} (Tallverdi: {kort1.get_tallverdi()})\n{spiller2} trakk: {kort2} (Tallverdi: {kort2.get_tallverdi()})")
        
    def vinner(self): # 
        if self.spiller1.get_seiere() > self.spiller2.get_seiere():
            return f"{self.spiller1.navn} vant med {self.spiller1.get_seiere()} seiere mot {self.spiller2.navn}s {self.spiller2.get_seiere()}."
        elif self.spiller1.get_seiere() < self.spiller2.get_seiere():
            return f"{self.spiller2.navn} vant med {self.spiller2.get_seiere()} seiere mot {self.spiller1.navn}s {self.spiller1.get_seiere()}."
        else:
        	return "Det ble uavgjort!"

    def spill_krig(self):
        print("\nLa spillet begynne!\n")
        
        while len(self.kortstokk.kort) >= 2: # Kjører så lenge det er nok kort
            svar = input('Skriv "S" for å starte runden eller "A" for å avslutte: ').lower()
            if svar == "a":
                break # Hopper ut av løkken hvis spilleren skriver "A"
            
            # Lagrer kortene
            kort1 = self.kortstokk.dele_ut_kort()
            kort2 = self.kortstokk.dele_ut_kort()
            
            # Lagrer spillernavn
            spiller1 = self.spiller1.navn
            spiller2 = self.spiller2.navn
            
            # Skriver ut hva som har blitt trukket
            self.print_kort(spiller1, kort1, spiller2, kort2)

            # Hvis kortene er like kjører denne krig-løkken
            while kort1.get_tallverdi() == kort2.get_tallverdi():
                print("Kortene er like. Det er tid for krig!")
                print("\n1...\n2...\n3...\n\nKRIG!")
                hånd = self.kortstokk.dele_ut_hånd(6)
                kort1 = self.kortstokk.dele_ut_kort()
                kort2 = self.kortstokk.dele_ut_kort()
                self.print_kort(spiller1, kort1, spiller2, kort2)
            if kort1.get_tallverdi() > kort2.get_tallverdi(): # Hvis ikke kalles .seiere-metoden for å øke ant. seiere
                self.seiere(spiller1)
            else:
                self.seiere(spiller2)

        print(self.vinner()) # Printer resultatet av "vinner-seremonien"

# Man trenger bare 2 linjer for å kjøre spillet, så jeg har ikke laget noen testfil.
# Uncomment disse linjene for å teste spillet:

spill = Krig()
spill.spill_krig()