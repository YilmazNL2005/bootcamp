# Definieer drie variabelen var1, var2 en var3. Bereken het gemiddelde en
# stop het in een variabele gemiddelde. Toon het gemiddelde. Voeg drie commentaren toe.
# Pas het programma nu zo aan dat de gebruiker getallen kan invoeren.

var1 = int(input("Vul een getal in. "))
var2 = int(input("Vul een getal in. "))
var3 = int(input("Vul een getal in. "))
totaal = var1 + var2 + var3
gemiddelde = totaal / 3
print("Het gemiddelde is: "+ str(gemiddelde))