Frase = input()

Dicionario = {}

FraseStrip = Frase.strip()
FraseSpaces = FraseStrip.split(" ")

for x in FraseSpaces:
    countFrase = len(x)
    Dicionario[x] = countFrase

print(Dicionario)












