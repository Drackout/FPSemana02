Word1 = input()
Word2 = input()

interWord =""

SetPalavra1 = set()
SetPalavra2 = set()

for i in Word1:
    SetPalavra1.add(i)

for j in Word2:
    SetPalavra2.add(j)

for k in SetPalavra1.intersection(SetPalavra2):
    interWord += k

print(interWord)