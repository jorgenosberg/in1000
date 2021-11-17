'''
Skriv en program som program som ber brukeren om å gjøre enkle beregninger 
(for eksempel: 1 + 1, 5 * 4, 10 / 2).
Hver gang brukeren gir det riktige svaret, blir det neste spørsmålet stilt. 
Hvis brukeren gir et feil svar, skriv ut "du tapte!", 
hvis brukeren svarer på alle spørsmålene riktig, skriv ut "du vant!"
'''

regnestykker = ["Hva er 1 + 1?", "Hva er 5 * 4?", "Hva er 10 / 2?"]
status = True
fasit = [2, 20, 5]
teller = 0

print("Du vil nå bli bedt om å sv")

while status:
    print(regnestykker[teller])
    svar = int(input())
    if svar != fasit[teller]:
        status = False
    teller += 1

