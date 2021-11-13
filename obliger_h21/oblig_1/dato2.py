'''
Oblig 1 | IN1000 | Høsten 2021

Filnavn: dato2.py

Dette er den frivillige ekstraoppgaven i første oblig, der jeg skal
vise hvordan man forenkle datosammenlikningen fra oppgave 3.
Målet er å la brukeren oppgi hver av de to datoene som ett tall.

27.08: Oppdatert med int() rundt dato-variablene for at Python alltid skal lese 
inputen som heltall.

29.08: Har oppdaget at programmet ikke fungerer som det skal. Ikke så overraskende - 
jeg har glemt å bytte format fra DD.MM til MM.DD. Hvis dato1 starter
den 10. eller senere, vil datovariabelen få høyere tallverdi enn en dato som egentlig
er senere. Tilbakemeldingen blir dermed feil.

Løsning: Be bruker om datoer i formatet MM.DD. Dermed sammenlikner Python måneden først,
deretter dagen. Større tallverdi = senere dato.

Jeg inkluderer kun løsningen i denne filen. Feilen min kan ses i tidligere versjoner.
'''

# Få datoer fra bruker
print("Vennligst skriv inn to valgfrie datoer. Bruk fire sifre i formatet MM.DD. For eksempel tilsvarer 12. september tallet 0912. 4. januar tilsvarer tallet 0104")
dato1 = int(input("Første dato: "))
dato2 = int(input("Andre dato: "))

# Sjekke om bruker har tastet inn korrekt dato
def checkNums:
	if dato1.isnumeric() == False:
		print("Du har tastet inn bokstaver. Vennligst bare bruk tall.")
	elif dato2.isnumeric() == False:
		print("Du har tastet inn bokstaver. Vennligst bare bruk tall.")

def checkDate:
	

# Sjekke hvilken dato som kommer først
if dato1 < dato2:
	print("Riktig rekkefølge!")
elif dato1 == dato2:
	print("Samme dato!")
else:
	print("Feil rekkefølge!")
