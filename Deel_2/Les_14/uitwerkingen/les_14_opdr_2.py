getallen = [1, 2, 3, 10, 5]
print(getallen)
getal_verwijderen = int(input("Welk getal wil je uit de lijst verwijderen? "))
print(f"Het getal: {getallen[getal_verwijderen]}")
getallen.pop(getal_verwijderen)
print(getallen)