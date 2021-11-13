'''
Oblig 4 | IN1000 | Høst 2021

Filnavn: ordtelling.py

KLAR FOR RETTING!

Dette programmet skal lage to funksjoner som kan telle antall bokstaver i et ord og
antall ord i en setning. Ved hjelp av disse to funksjonene skal programmet hente en
setning fra brukeren og fortelle hvor mange bokstaver som er i hvert ord, hvor mange
ord som er i setningen, og hvor mange ganger hvert ord forekommer i setningen.

Jeg har bevisst valgt å lage et program som ikke er case sensitive. Dermed blir alle 
ord med samme bokstaver regnet som det samme ordet, uavhengig av plassering i setningen
og store/små bokstaver.

'''

### OPPGAVE 4.1 ###

# Definere en funksjon som teller antall bokstaver i et ord
def countLetters(et_ord):
    return len(et_ord)

### OPPGAVE 4.2 ###

# Lage en funksjon for å sjekke antall forekomster av et ord i en ordbok
def dictWords(en_setning):
    antall_ganger = dict()
    alle_ord = en_setning.lower() # Bruker str.method lower() for at alle like ord skal samles uavh. av upper/lower
    alle_ord = alle_ord.split()
    
    for ord in alle_ord:
        if ord in antall_ganger:
            antall_ganger[ord] += 1
        else:
            antall_ganger[ord] = 1
    
    return antall_ganger

# Teste funksjonen på en enkel setning
# print(dictWords("Hei hei , obligretter ! Hvordan går det ?")) 

### OPPGAVE 4.3 ###

# Hente en setning fra brukeren
setning = input("Skriv inn en valgfri setning: ")

# Fortell brukeren hvor mange ord som er i setningen
print(f"Det er {len(setning.split())} ord i setningen din.")

# Fortell brukeren hvor mange ganger hvert ord forekommer
dict_setning = dictWords(setning)

for key in dict_setning:
    print(f"Ordet '{key.upper()}' forekommer {dict_setning[key]} ganger, og har {countLetters(key)} bokstaver.")

    # Her bruker jeg .upper() for å gjøre det enda lettere å se hvilket ord som er i fokus