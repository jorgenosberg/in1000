'''
Oblig 5 | IN1000 | Høst 2021

Filnavn: temperatur.py

KLAR FOR RETTING!

Dette programmet skal åpne og hente data fra to .csv-filer
som inneholder månedlige temperaturmålinger fra 1750-2017 og
daglige temperaturmålinger fra 2018.

I programmet skal jeg definere én funksjon som henter data fra
filen og returnerer en ordbok og én prosedyre som går gjennom en og
en temperatur, finner makstemperaturene, og oppdaterer ordboken
med nye varmerekorder.
'''

### OPPGAVE 1 ###

# Definere en fil-til-ordbok-funksjon for å lese .csv-filen og returnere en ordbok med innholdet 
def fileToDict(fil):
    
    # Lage en tom ordbok
    ordbok = dict()
    
    with open(fil) as file:
        # For-løkke for å iterere gjennom filen og dele opp
        for linje in file:
            kolonner = linje.split(",") # Splitter ved komma fordi det er .csv
            ordbok[kolonner[0]] = float(kolonner[1])
    
    # Returnerer ordboken
    return ordbok

# Skrive ut resultatet fra funksjonen, altså ordboken
print(fileToDict("max_temperatures_per_month.csv"))

### OPPGAVE 2 og OPPGAVE 3 ###

# Lage en prosedyre for å finne høyeste temperatur
def checkHighestTemp(ordbok, fil):
    
    with open(fil) as file:
        for linje in file:
            kolonner = linje.split(",") # Splitter på komme pga. .csv
            måned = kolonner[0] # Indekserer første kolonne som måned
            dag = int(kolonner[1]) # Indekserer int av andre kolonne som dag
            temperatur = float(kolonner[2]) # Indekserer float av tredje kolonne som temp

            # Sammenligner nye temperaturer med den andre ordboken og oppdaterer ordboken
            if temperatur > ordbok[måned]:
                print(f"Ny varmerekord ble satt {str(dag)}. {måned}, da temperaturen nådde {str(temperatur)} grader Celsius (gammel rekord var {str(ordbok[måned])} grader).")
                ordbok[måned] = temperatur
    
    # Returnerer den nye, oppdaterte ordboken
    return ordbok

# Lagre ordboken fra den første funksjonen for å teste prosedyren
maksTemperaturer = fileToDict("max_temperatures_per_month.csv")

# Sjekke checkHighestTemp-funksjonen med ordboken
print(checkHighestTemp(maksTemperaturer, "max_daily_temperature_2018.csv"))
maksTemperaturer = checkHighestTemp(maksTemperaturer, "max_daily_temperature_2018.csv")

### BONUS: OPPGAVE 4 ###

# Definere en prosedyre som  skriver ordboken til en ny fil
def exportDict(ordbok, filnavn):
     
    with open(filnavn, "w") as fil: # Åpne filen i "write"-modus
        # Skriver ut hver nøkkelverdi og innholdsverdi med komma-separator og linjeskift
        for måned in ordbok:
            fil.write(måned + "," + str(ordbok[måned]) + "\n")

# Teste prosedyren og se at filen ser riktig ut
exportDict(maksTemperaturer, "max_temp_monthly_updated.csv")

### BONUS: OPPGAVE 5 ###

# Funksjon som finner månedsnummeret fra forkortelsene i filen
def monthToNum(måned):
    måneder = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return måneder.index(måned) + 1

# Funksjon som oversetter formatert Datetime-dato til norsk
def engToNor(dato):
    dager = {"Monday":"mandag", "Tuesday":"tirsdag", "Wednesday":"onsdag",
             "Thursday":"torsdag", "Friday":"fredag", "Saturday":"lørdag", "Sunday":"søndag"}
    måneder = {"Jan":"januar", "Feb":"februar", "Mar":"mars", "Apr":"april",
               "May":"mai", "Jun":"juni", "Jul":"juli", "Aug":"august", "Sep":"september",
               "Oct":"oktober", "Nov":"november", "Dec":"desember"}
    return f"{dager[dato.split()[0]]} {dato.split()[1]} {måneder[dato.split()[2]]}"

# Importerer biblioteket datetime for å jobbe med datoer
import datetime as dt

def checkHeatwave(fil):

    datoer = list() # Tom liste jeg kan putte datoene inn i senere
    sammenhengende = 0 # Teller-variabelen til logikken i for-løkken
    
    # Åpner filen, splitter og lagrer som i oppg. 2
    for linje in open(fil):
        kolonner = linje.split(",") 
        måned = kolonner[0]
        dag = int(kolonner[1])
        temperatur = float(kolonner[2])
    
        # If-test for å sjekke om temperaturen er over 25
        if temperatur > 25:
            sammenhengende += 1 # Legger til 1 til teller-variabelen
        else: # Hvis temp != 0, gå til else
            if sammenhengende >= 5: # Hvis det er >= 5 dager på rad
                slutt = dt.date(2018, monthToNum(måned), dag) # Lage dato-variabler
                start = slutt - dt.timedelta(days = sammenhengende) # Trekke fra teller-variabelen for å finne startdatoen
                slutt = slutt - dt.timedelta(days = 1) # Trekke fra én dag for å finne slutt-datoen
                slutt = str(slutt.strftime("%A %d. %b")) # Formatere vha. datetime
                start = str(start.strftime("%A %d. %b"))
                start = engToNor(start) # Oversette til norsk
                slutt = engToNor(slutt)
                datoer.append([start, slutt]) # Legge inn datoene i den tomme listen
                sammenhengende = 0 # Setter teller-variabelen til 0 for å gå videre til neste hetebølge
            else:
                sammenhengende = 0 # Setter teller-variabelen til 0 fordi det ikke var >= 5 på rad
    
    # For-løkke for å skrive ut informasjonen til brukeren
    print(f"Det var {len(datoer)} hetebølger i 2018.")
    for x in range(len(datoer)):
        print(f"En hetebølge startet {datoer[x][0]} og sluttet {datoer[x][1]}.")

# Tester funksjonen med riktig fil
checkHeatwave("max_daily_temperature_2018.csv")