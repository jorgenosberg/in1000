'''
Oppgave 01.18:

Skriv et program som spør brukeren om å taste inn tre forskjellige tall, og lagrer dem i tre variabler.

1) Skriv ut største verdien av de tre.
2) Skriv ut hvor mange av de tre tall er lik den største verdien. (f.ex. hvis tallene er 1, 3, 3; største verdien er 3 og 2 tall er lik 3) (vanskelig!)

Hint: verdien av en variabel kan 'kopieres' til en annen variabel. For eksempel når vi skriver:
a = 1
b = a
dette betyr at b også inneholder verdi 1.
'''

# Be brukeren om å taste inn 3 forskjellige tall
print("Du vil nå bli bedt om å taste inn tre tall.")
num1 = int(input("Tall 1: "))
num2 = int(input("Tall 2: "))
num3 = int(input("Tall 3: "))

# Lage liste med de tre tallene
nums = [num1, num2, num3]

# Skrive ut det største tallet
print(max(nums))

# Sjekke hvor mange tall som er like som den største verdien




