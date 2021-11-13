


def lagBrukernavn(navn):
    return navn.split()[0].lower() + navn.split()[1][0].lower()

print(lagBrukernavn("Kari Nordmann"))

def lagEpost(prefix, suffix):
    return prefix + "@" + suffix

print(lagEpost("martineher", "uio.no"))

lagEpost(prefix = "martineher", suffix = "uio.no")

prefix = input("Skriv inn brukernavn: ")
suffix = input("Skriv inn e-post-suffix: ")

print(lagEpost(prefix, suffix))

assert lagEpost("karin", "student.matnat.uio.no") == "karin@student.matnat.uio.no"



