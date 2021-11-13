'''
Oblig 2 | IN1000 | Høsten 2020

Filnavn: fahrenheit_celsius.py

Dette programmet svarer på oppgave 2 i andre oblig i IN1000. 
Målet er å skrive et program som kan konvertere en temperatur 
i fahrenheit til celsius.
'''

# Deloppgave 1:
# Definere en fahrenheit-variabel med en tilfeldig temperatur
# fahrenheit = 110

# Endring fra deloppgave 5:
fahrenheit = int(input("Oppgi en temperatur i fahrenheit: "))

# Skrive ut den valgte temperaturen
print(f"Temperaturen i fahrenheit er: {fahrenheit}")

# Regne ut celsius-variabelen
celsius = (fahrenheit - 32) * 5 / 9

# Ekstra - runde av til to desimaler:
celsius = round(celsius, 2)

# Skrive ut resultatet i celsius
print(f"{fahrenheit} grader fahrenheit tilsvarer {celsius} grader celsius.")