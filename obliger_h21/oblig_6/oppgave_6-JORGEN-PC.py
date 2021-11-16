'''
Oblig 6 | IN1000 | Høst 2021

Filnavn: oppgave_6.py

KLAR FOR RETTING!

'''
from random import shuffle

class Kort:
	def __init__(self, farge, verdi): # Henter verdi og farge fra Kortstokk-klassen når den opprettes
		self.farge = farge
		self.verdi = verdi

	def __repr__(self): # Returnerer verdi og farge på kortet som en streng. Eks: "Hjerter 10"
		return f"{self.farge} {self.verdi}"

class Kortstokk:
	def __init__(self):
		farger = ["Hjerter", "Ruter", "Kløver", "Spar"]
		verdier = ["Ess","2","3","4","5","6","7","8","9","10","Knekt","Dronning","Konge"]
		self.kort = [Kort(farge, verdi) for farge in farger for verdi in verdier]

	def __repr__(self):
		return f"En kortstokk med {self.tell_kort()} kort"

	def tell_kort(self):
		return len(self.kort)

	def stokke(self): # Bruker shuffle fra random-biblioteket for å stokke kortstokken
		if self.tell_kort() < 52: # Sjekker at kortstokken
			raise ValueError("Kun hele kortstokker (52 kort) kan bli stokket.")
		shuffle(self.kort)
		return self

	def _dele_ut(self, antall):
		count = self.tell_kort()
		# Sjekker hva som er minst av antall og rest. kort og bestemmer maks kort som kan deles ut
		maks = min([count, antall]) 
		if count == 0: # Sjekker om det er flere kort igjen, gir error hvis kortstokken er tom
			raise ValueError("Alle kortene har blitt delt ut.")
		kort = self.kort[-maks:]
		self.kort = self.kort[:-maks]
		return kort

	def dele_ut_kort(self):
		return self._dele_ut(1)[0]

	def dele_ut_hånd(self, hand_size):
		return self._dele_ut(hand_size)

kortstokk = Kortstokk()

print(kortstokk)

kort = kortstokk.dele_ut_kort()

print(kort)