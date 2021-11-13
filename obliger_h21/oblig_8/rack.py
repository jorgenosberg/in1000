'''
Oblig 8 | IN1000 | Høst 2021

Filnavn: rack.py
Oppgave: 2

Denne filen svarer på oppgave 2 i oblig 8, og inneholder klassedefinisjonen
med grensesnitt og implementasjon for klassen Rack.

Rack skal kunne ta imot instanser av klassen Node, og skal tilby metoder
som kan sette inn Noder, sjekke minnekapasitet og ellers returnere informasjon
om nodene i racket.

Basert på grensesnittet som er oppgitt i grensesnitt.py og utvidet i henhold til
oppgaven.
'''

# Definisjon av klassen Rack, en "hylle" som skal ta imot instanser av Node
class Rack:
    
	# Oppretter et rack der det senere kan plasseres noder
	#	@param ingen parametre
	#	@instansvariabel _noder = liste der nodene skal plasseres
	#	@return None
	def __init__(self) -> None:
		self._noder = list()
  
	# Oppretter en representasjons-metode som gir en lesbar streng med info om racket.
	#	@param ingen parametre
	#	@return string med info om instansen
	def __repr__(self) -> str:
		return f"(Rack med {self.getAntNoder()} noder, {self.antProsessorer()} prosessorer og {self.getTotMinne()} GB minne)"
 
 	# Oppretter en string-metode som gir info om instansen når man kaller på str(instans)
	#	@param ingen parametre
	#	@return string med info om instansen
	def __str__(self) -> str:
		return f"(Rack med {self.getAntNoder()} noder og {self.antProsessorer()} prosessorer og {self.getTotMinne()} GB minne)"
		
	# Prosedyre-metode som setter en ny node inn i racket
	#	@param node = noden som skal plasseres inn
	#	@return None
	def settInn(self, node) -> None:
		self._noder.append(node)

	# Getter som sjekker antall noder i racket
	#	@param ingen parametre
	#	@return antall noder i listen self._noder
	def getAntNoder(self) -> int:
		return len(self._noder)

	# Beregner sammenlagt antall prosessorer i nodene i et rack
	#	@param ingen parametre
	#	@return antall prosessorer for alle noder i self._noder
	def antProsessorer(self) -> int:
		return sum([node.antProsessorer() for node in self._noder])

	# Beregner antall noder i racket med minne over gitt grense
	#	@param paakrevdMinne = antall GB minne som kreves
	#	@return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne) -> int:
		return len([node for node in self._noder if node.nokMinne(paakrevdMinne) == True])

	### EKSTRA METODER ###
 
 	# Getter som sjekker totalt minne i racket
	#	@param ingen parametre
	#	@return int av total minnekapasitet
	def getTotMinne(self) -> int:
		return sum([node.getMinne() for node in self._noder])