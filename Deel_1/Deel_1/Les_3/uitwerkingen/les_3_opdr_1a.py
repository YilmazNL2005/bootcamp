aantal_studenten = int(input("Hoeveel studenten zijn er in jouw klas? "))
collegegeld = int(input("Wat is het collegegeld voor dit studiejaar? "))

totaalbedrag = aantal_studenten * collegegeld

print("In jouw klas zitten: " + str(aantal_studenten) + "studenten. Het collegegeld is voor elke student dit jaar: " + str(collegegeld) + "euro.") 
print("In totaal betaal je met z'n allen voor dit studiejaar: " + str(totaalbedrag) + "euro." )