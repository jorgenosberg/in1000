'''
Skriv et program som spør brukeren om å taste inn favorittfargen.
Hvis den er gul, oransje eller grønn, skriv ut navnet på en frukt som har den fargen.
'''

farge = input("Skriv inn favorittfargen din: ").lower()
farger = {"gul": "Pakistansk mango", 
          "oransje": "Appelsin",
          "grønn": "Kiwi"}

if farge in farger:
    print(farger[farge])