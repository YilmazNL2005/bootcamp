import random

while True:
    getal = random.randint(1,5)
    print(getal)
    raden = int(input("Geef een getal op tussen de 1 en 5. "))
    if getal == raden:
        print("Je hebt het getal goed geraden!")
        break
    else:
        print("Je hebt het getal niet goed geraden!")