'''
Skriv et program som spør brukeren om å taste inn tre forskjellige tall, og lagrer dem i tre variabler.

1) Skriv ut største verdien av de tre.

2) Skriv ut hvor mange av de tre tall er lik den største verdien. (f.ex. hvis tallene er 1, 3, 3; største verdien er 3 og 2 tall er lik 3) (vanskelig!)

Hint: verdien av en variabel kan 'kopieres' til en annen variabel. For eksempel når vi skriver:
a = 1
b = a
dette betyr at b også inneholder verdi 1.

'''

tall1 = int(input("Tast inn et tall: "))
tall2 = int(input("Tast inn et tall: "))
tall3 = int(input("Tast inn et tall: "))

tall = [tall1, tall2, tall3]

def condition(x, tall):
    return x == max(tall)

print(sum(condition(x, tall) for x in tall))
