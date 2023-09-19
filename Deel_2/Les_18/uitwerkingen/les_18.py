import random

getallen = [1, 2, 3, 4, 5]

aantal_rondes = 1
antwoorden_fout = 0
doorgaan = "ja"
while doorgaan == "ja":
    getal = random.randint(1,5)
    print(getal)
    raden = int(input("Geef een getal op tussen de 1 en 5. "))
    if getal == raden and raden in getallen:
        print("Je hebt het getal goed geraden!")
        doorgaan = input("Wil je nog een ronde spelen? ja / nee ")
        if doorgaan == "ja":
            aantal_rondes += 1
        else:
            print(f"Je hebt {aantal_rondes} rondes gespeeld en {antwoorden_fout} foute antwoorden.")
    elif raden not in getallen:
        print("Dit is geen getal die je kunt kiezen.")
    else:
        print("Je hebt het getal niet goed geraden!")
        antwoorden_fout += 1