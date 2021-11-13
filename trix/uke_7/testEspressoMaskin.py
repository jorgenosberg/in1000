from oppg_7_03 import EspressoMaskin

def hovedprogram():
    
    # Opprette en kaffemaskin med 1L tank
    kaffe = EspressoMaskin(1000)
    kaffe.fyllVann(40)

    # Hent kommandoer fra brukeren
    kommando = input('Hva slags kaffe vil du ha i dag?\nSkriv "E" for espresso, "L" for lungo eller "A" for å avslutte: ')
    
    while kommando not in ["E", "L", "A"]:
        print('Feil input!')
        kommando = input('Skriv "E" for espresso, "L" for lungo eller "A" for å avslutte: ')
        
    if kommando == "E":
        kaffe.lagEspresso()
        print(f"Det er nå {kaffe.hentVannmengde()} ml på tanken.")
    elif kommando == "L":
        kaffe.lagLungo()
        print(f"Det er nå {kaffe.hentVannmengde()} ml på tanken.")
    elif kommando == "A":
        print("Ha en fortsatt fin dag!")
            
    # kaffe.lagEspresso()

    # kaffe.fyllVann(100)

    # kaffe.lagEspresso()

    # kaffe.lagLungo()

    # kaffe.fyllVann(1500)

    # kaffe.lagLungo()
    
hovedprogram()