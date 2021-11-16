'''
Oblig 1 | IN1000 | Høsten 2021

Filnavn: dato.py

Dette er oppgave 3 i første oblig, og den skal vise at jeg kan
bruke en if-test for å sjekke hvilken dato som kommer først i et år.

27.08: Oppdatert med int() rundt dato-variablene for sikkerhets skyld.
'''

# Be om to datoer fra brukeren
print("Vennligst oppgi en valgfri dato med tall. Skriv dag først, deretter måned. Eksempel: 14 og 4 for 14. april. NB! Ikke skriv '0' foran dager eller måneder.")
dag1 = int(input("Dag: "))
måned1 = int(input("Måned: "))

print("Legg nå inn en ny dato på samme måte.")
dag2 = int(input("Dag: "))
måned2 = int(input("Måned: "))

# Gjøre en if-test av datoene med tilbakemelding til bruker
if måned1 < måned2:
	print("Riktig rekkefølge!")
elif måned1 == måned2 and dag1 < dag2:
	print("Riktig rekkefølge!")
elif måned1 == måned2 and dag1 == dag2:
	print("Samme dato!")
else:
	print("Feil rekkefølge!")