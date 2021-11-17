'''
Skriv et program som spør brukeren om deres matpreferanser for å finne et godt måltid for dem. 
Bruk minst to matpreferanser, for eksempel kjøttspiser/vegetarianer/veganer og glutenallergi/ingen allergi.

Du kan bruke følgende måltider som eksempelmåltider. Noen måltider kan brukes i flere scenarier, og hvert måltid bør brukes minst en gang.

    Falafal (vegetarisk og vegansk, glutenfri)
    Lasagne (inneholder kjøtt, gluten)
    Steik (inneholder kjøtt, glutenfri)
    Pizza margherita (vegetarisk, men ikke vegansk, inneholder gluten)

Brukeren kan svare 'ja' eller 'nei'. Hvis du får et annet svar, skriv ut en advarsel.
'''

matpreferanser = list()

matpreferanser.append(input("Vennligst oppgi om du er 'kjøttspiser' / 'vegetarianer' / 'veganer'? ").lower())
matpreferanser.append(input("Vennligst oppgi om du har 'glutenallergi' / 'ingen allergi'? ").lower())

måltider = {
    "Falafel": ["vegetarianer", "veganer", "glutenallergi"],
    "Lasagne": ["kjøttspiser", "ingen allergi"],
    "Steik": ["kjøttspiser", "glutenallergi"],
    "Pizza margherita": ["vegetarianer", "veganer", "ingen allergi"]
}

    