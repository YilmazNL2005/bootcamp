woorden = []
for x in range(5):
    woord_toevoegen = input("Welk woord wil je toevoegen aan de lijst? ")
    woorden.append(woord_toevoegen)
    for y in range(0, len(woorden)):
        print(woorden[y], "\n")