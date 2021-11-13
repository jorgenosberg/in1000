'''
Oblig 3 | IN1000 | Høst 2021

Filnavn: oppgave_5.py

KLAR FOR RETTING!

I denne oppgaven skal du ved hjelp av Pythons ordbok-format lage en PokéDict, altså en ordbok som inneholder 
en oversikt over Pokémon og deres evolusjoner.

Gjør nytte av Web Scraping-verktøy for å hente en liste over alle de 151 Pokémonene fra første generasjon
(Kanto-regionen) og sorter dem i en ordbok etter utviklinger. Sett første Pokémon som nøkkelverdi og 
mulige utviklinger for hver Pokémon som innholdsverdier.

Til slutt skal du la brukeren skrive inn navnet på en Pokémon og fortelle brukeren hvilke utviklinger den
valgte Pokémonen har.
'''

# Importere de nødvendige pakkene for å håndtere
import requests
import pandas as pd
import numpy as np

# Jeg setter URLen jeg ønsker å scrape
url = "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon_by_evolution"

# Jeg henter DataFramen fra HTML-koden vha. Pandas
dfs = pd.read_html(url)

# Jeg forsikrer meg om at jeg kun bruker den første DataFramen (table) 
pokemon = dfs[0]

# Jeg fjerner alle rader over 78 for å kun bruke Pokémon fra første generasjon
pokemon = pokemon[:78]

# Jeg fjerner den ekstra kolonnen med tall fordi Pandas automatisk gir radene tallverdier
del pokemon[pokemon.columns[0]]

# Jeg rydder opp i navnene på kolonnene for å forenkle to_dict-prosessen
pokemon.rename(columns={'Unevolved Pokémon/Basic Pokémon': 'Pokémon', 
                        'First-Evolved Pokémon/Stage 1 Pokémon': 'Første utvikling', 
                        'Second-Evolved/Stage 2': 'Andre utvikling'}, inplace = True)

# Jeg bytter ut Numpy NaN-verdiene som er standard i Pandas for å jobbe med None i stedet
pokemon = pokemon.replace({np.nan: None})

# Jeg konverterer den formaterte DataFramen til en Python-ordbok
poke_dict = pokemon.set_index('Pokémon').T.to_dict('list')

# Jeg henter input fra brukeren og lagrer det som valgt_pokemon
valgt_pokemon = input("Velg en Pokémon: ").capitalize()

# Jeg tester inputen opp mot ordboken og forteller brukeren resultatet vha. concatenation og formatted strings.
if valgt_pokemon in poke_dict.keys():
    if poke_dict[valgt_pokemon] == [None, None]:
        print(valgt_pokemon + " har ingen utviklinger.")
    elif None in poke_dict[valgt_pokemon]:
        print(f"{valgt_pokemon} har kun én utvikling: {poke_dict[valgt_pokemon][0]}")
    else:
        print(f"{valgt_pokemon} har utviklingene {poke_dict[valgt_pokemon][0]} og {poke_dict[valgt_pokemon][1]}")
else:
    print("Pokémonen du oppga finnes ikke i vår PokéDict. Kontroller at du har stavet navnet riktig.")