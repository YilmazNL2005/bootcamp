naam = input("Hoe heet je? ")
leeftijd = int(input("Wat is je leeftijd in jaren? "))
verschil = leeftijd - 18

if leeftijd >= 18:
    print("Dag "+str(naam)+", Je bent " +str(verschil)+" jaar ouder dan 18.")
if leeftijd >= 18 and leeftijd <= 20:
    print("Kan je mij je legitimatie geven? ")
else:
    print("Sorry "+str(naam)+" Je bent onder de 18 dus je mag geen alcohol kopen.")