'''
Oblig 1 | IN1000 | Høst 2021

Filnavn: beslutninger.py

Dette er andre oppgave i første oblig, der jeg skal vise at
jeg kan bruke input()-funksjonen og if-statements.
'''

# Hente svar fra brukeren
svar = input("Vil du ha en brus? ").lower()

	# Merk at jeg bruker lower() for å kun returnere brukerens
	# svar i lowercase. Da blir if-testen enklere.

# Sjekke og reagere på svaret
if svar == "ja":
	print("Her har du en brus!")
elif svar == "nei":
	print("Den er grei.")
else:
	print("Det forstod jeg ikke helt.")


