filnavn = "saga.txt"
navn = filnavn.removesuffix(".txt")
noderPerRack = 0

with open(filnavn) as fil:
    innhold = fil.read()
    deler = innhold.split()
    noderPerRack = deler[0]
    node1 = deler[1:4]
    node2 = deler[4:]

