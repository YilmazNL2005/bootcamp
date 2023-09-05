appels = float(input("Hoeveel heb je betaald aan appels? "))
druiven = float(input("Hoeveel heb je betaald aan druiven? "))
bananen = float(input("Hoeveel heb je betaald aan bananen? "))

totaal = appels + druiven + bananen
prijs_excl_btw = totaal / 109 * 100
prijs_incl_btw = totaal / 79 * 100
print("De totaalprijs voor Appels, Druiven en bananen excl btw: "+ str(prijs_excl_btw) +" euro.")
print("De totaalprijs voor Appels, Druiven en bananen incl btw: "+ str(prijs_incl_btw) +" euro.")