collegegeld_pp = int(input("Hoeveel collegegeld moet elke student betalen voor dit studiejaar? "))
aantal_studenten = int(input("Hoeveel studenten zitten er in jouw groep? "))
totaal_bedrag_collegegeld = collegegeld_pp * aantal_studenten
print("In totaal voor: "+ str(aantal_studenten)+ " studenten, moet er: "+str(totaal_bedrag_collegegeld)+ " euro betaald worden.")


appels = 3.40
druiven = 2.45
bananen = 1.95
totaalprijs = appels + druiven + bananen
totaalprijs_excl_btw = totaalprijs / 109 * 100
totaalprijs_incl_btw = totaalprijs / 100 * 109

print("De totaalprijs excl btw voor de appels, druiven en bananen: " +str(totaalprijs_excl_btw)+ " euro. De totaalprijs is incl btw: " +str(totaalprijs_incl_btw)+" euro.")