# Opdracht 1 (schrijf je antwoord als commentaar in een py file):


# a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad (kladblok)? Noem de voordelen!
# Antwoord: Met Vsc kan je fouten of errors veel sneller ontdekken dan in kladblok. 
# In kladblok kan je je geschreven code niet testen en Vsc kan dat wel.

# b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?
# Antwoord: Zodat je opdrachten/werk veilig opgeslagen is en altijd en overal terug kunt halen. 
# Daarnaast is het handig voor de docenten want zij kunnen dan de voortgang van je werk bekijken en volgen.
# Nog een voordeel. Stel je laptop gaat kapot met al je bestanden met code, dan kun je dat altijd terugkrijgen van Github.


# Opdracht 2:
# Maak het commentaar af.
#   a = 5  # dit is een voorbeeld van het datatype: Int
#   b = 10.5# dit is een voorbeeld van het datatype: Float
#   c = "Hallo wereld" # dit is een voorbeeld van het datatype: String


# Opdracht 3:
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
# a = 5
# b = 10
# voeg jouw code toe…
# wissel_waarden = a,b = b,a
# Controleer met onderstaande code of de waarden correct zijn verwisseld
# print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen


# Opdracht 4:

# Los de problemen op (zonder exception handling).
# leeftijd = int(input("Hoe oud ben je?"))

# print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!


# Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
# def som(a, b, c):
#     berekening = a + b + c
#     return berekening


# getal1 = 200
# getal2 = 5
# getal3 = 12
# antwoord = som(getal1, getal2, getal3)# of de naam van je eigen functie.
# print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")


#Opdracht 6:
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True

aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if ONBEPERKT == True:
    print("Je hoeft je nergens druk om te maken, je hebt onbeperkt GB en bellen.")
elif aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB:
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")
# Ik kan ook de if op regel 63 met de print van regel 64 weghalen en 
# de else van regel 67 een elif maken die checkt of het een onbeperkt abonnement is of niet plus of je niet teveel verbruikt hebt.