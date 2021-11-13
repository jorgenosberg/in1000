'''
a) Skriv en funksjon vanligKonkat som konkatenerer to lister. Dersom du har to lister (to argumenter): ["a", "b", "c"] og [1, 2, 3], 
skal listen som funksjonen returnerer se slik ut: ["a", "b", "c", 1, 2, 3].

b) Skriv funksjonen annenhverKonkat som konkatenerer to lister slik: gitt ["a", "b", "c"] og [1, 2, 3] s
om argumenter så skal funksjonen returnere listen: ["a", 1, "b", 2, "c", 3]. Du kan anta at gitt listene er av samme lengde.

c) Skriv en funksjon tallTilListe som returnerer en liste med siffer gitt et tall. 
Dvs. tallet 895 skal returnere listen [8, 9, 5]. (Hint: du kan konvertere tallet til en annen datatype)
'''

# Oppgave a)

def vanligKonkat(liste1, liste2):
    return liste1 + liste2
    
print(vanligKonkat(["a", "b", "c"], [1, 2, 3]))

# Oppgave b)

def annenhverKonkat(liste1, liste2):
    liste3 = []
    for x in range(len(liste1)):
        liste3.append(liste1[x])
        liste3.append(liste2[x])
    return liste3

print(annenhverKonkat(["a", "b", "c"], [1, 2, 3]))

# Oppgave c)

def tallTilListe(tall):
    liste = []
    for x in str(tall):
        liste.append(x)
    return liste

svar = input("Skriv hva som helst: ")

print(tallTilListe(svar))
