
Word1 = input()
Word2 = input()

intersection =""

SetPalavras = set()

for i in Word1:
    for j in Word2:
        if i == j:
            SetPalavras.add(i)

for k in SetPalavras:
    intersection += k


print(intersection)


