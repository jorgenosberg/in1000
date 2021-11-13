'''
Oblig 2 | IN1000 | Høst 2021

Filnavn: oppgave_5.py

Oppgavetekst:

Lag et enkelt tekstbasert spill som bruker if statements til å avgjøre hvem
som er vinneren. Eksempler på egnede spill er "stein, saks, papir" og "svart eller hvitt".

Programmet må fortelle brukeren om hen har vunnet eller tapt, og det må være mulig å spille igjen.
'''

# Jeg velger spillet stein, saks, papir

# Jeg vil lage en enkel CPU og importerer derfor randint()-funksjonen fra random-pakken
from random import randint

# Jeg definerer spillets logikk som en egen funksjon for å gjøre det enklere å spille igjen
def main():
    print("Stein...")
    print("Saks...")
    print("Papir...")

    # Jeg definerer en spillervariabel og registrerer brukerens valg
    player = input("Hva velger du? ").lower()

    # Jeg sjekker om valget er gyldig
    if player not in ("stein", "saks", "papir"):
        print('Feil input. Velg "stein", "saks" eller "papir"')
        player = input("Hva velger du denne gangen? ")

    # Jeg henter et tilfeldig tall fra randint()-funksjonen
    rand_num = randint(1, 3)

    # Jeg assigner tallet til stein, saks eller papir
    if rand_num == 1:
        computer = "stein"
    elif rand_num == 2:
        computer = "saks"
    else:
        computer = "papir"

    # Jeg informerer brukeren om hva maskinen valgte
    print("Du spiller mot datamaskinen i dag.")
    print(f"Maskinen valgte: {computer}")

    # Jeg sjekker hva brukeren og CPUen har valgt og erklærer en vinner
    if player == computer:
        print("Jasså? Ser ut som om det ble uavgjort. Prøv igjen!")
    elif player == "stein":
        if computer == "saks":
            print("Du vant! Premien er ære og berømmelse for alltid.")
        elif computer == "papir":
            print("Ikke verst! Maskinen er pent pakket inn i papir. Du vant!")
    elif player == "papir":
        if computer == "stein":
            print("Ikke verst! Maskinen er pent pakket inn i papir. Du vant!")
        elif computer == "saks":
            print("Chop chop. CPUen vant!")
    elif player == "saks":
        if computer == "stein":
            print("Jeg hører lyden av ødelagt metall. CPUen vant!")
        elif computer == "papir":
            print("Chop chop. Du vant!")
    else:
        print("Noe gikk galt...")

# Jeg caller funksjonen og lar brukeren spille 1 runde
main()

# Jeg gir brukeren muligheten til å spille igjen eller avslutte spillet
# Jeg bruker "not in" for å sikre at input blir riktig og "break" for å
# bryte løkken
while True:
    answer = input("Vil du spille igjen? (ja/nei): ").lower()
    if answer not in ('ja', 'nei'):
        print("Feil input.")
        answer = input("Vil du spille igjen? (ja/nei): ")
    if answer[0] == 'j':
        main()
    else:
        print("Takk for i dag!")
        break
