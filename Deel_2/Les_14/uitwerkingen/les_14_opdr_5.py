namen = ["yilmaz", "nora", "damian", "carolien", "jayden"]
for x in range(5):
    print(namen)
    naam_verwijderen = input("Welke naam wil je verwijderen uit de lijst? ")
    if naam_verwijderen in namen:
        namen.remove(naam_verwijderen)
    else:
        namen.append(naam_verwijderen)