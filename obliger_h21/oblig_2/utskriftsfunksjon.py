'''
Oblig 2 | IN1000 | Høst 2020

Filnavn: utskriftsfunksjon.py

Dette er oppgave 1 til andre obligatoriske innlevering i IN1000. 
Målet er å bruke en enkel prosedyre for å kunne kode om igjen og ha bedre 
struktur i programmet.
Jeg vil definere en prosedyre hilsen() for å lese inn og skrive ut informasjon
om flere personer.
'''

# Lage enkel prosedyre for å lese inn informasjon om 3 personer
def hilsen():
	navn = input("Hva heter du? ").capitalize()
	sted = input("Hvor kommer du fra? ").capitalize()
	print(f"Hei, {navn}! Du er fra {sted}.")

	# Merk at jeg bruker string-metoden .capitalize() for
	# å forsikre meg om at navn og stedsnavn begynner med stor bokstav.

# En løsning med string concatenation:
# def hilsen():
#     print("Hei, " + input("Hva heter du? ").capitalize() + "! "
#           "Du er fra " + input("Hvor kommer du fra? ").capitalize() + ".")

	# Selv foretrekker jeg imidlertid å jobbe med formatted strings.

# Kjør prosedyren tre ganger
hilsen()
hilsen()
hilsen()