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
# AANTAL_GB = 20 # Aantal GB data in je bundel
# AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
# ONBEPERKT = False # test ook met True

# aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
# aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
# if ONBEPERKT == True:
#     print("Je hoeft je nergens druk om te maken, je hebt onbeperkt GB en bellen.")
# elif aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB:
#     print("Let op: je moet bijbetalen!")
# else:
#     print("Niet aan de hand gebruik je mobiel lekker verder!")
# Ik kan ook de if op regel 63 met de print van regel 64 weghalen en 
# de else van regel 67 een elif maken die checkt of het een onbeperkt abonnement is of niet plus of je niet teveel verbruikt hebt.


#Opdracht 7:
# Print onder elkaar de getallen 1-250 met max 2 regels code.
# for getallen in range(1,251):
#     print(getallen)


# Opdracht 8:
# Gegeven is:

# lijst_eten = ['Onze menukaart:','appel', 'pannenkoek', 'kiwi', 'hamburger', 'granaatappelvlaaitaart']
# # for menu in range(len(lijst_eten)):
# #     print(lijst_eten[menu])
# # a: print een eenvoudig menu met de volgende layout:

#  Onze menukaart:
#  appel
#  pannenkoek
#  kiwi
#  hamburger 

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. 
# langste_string = 0
# for woord in range(1, len(lijst_eten)):
#     if len(lijst_eten[woord]) > langste_string:
#         langste_string = len(lijst_eten[woord])
#         grootste_eten = lijst_eten[woord]

# print("Het gerecht met de langste naam is: ", grootste_eten," met ", langste_string, " letters.")

#  Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). 
#  test je code door extra eten toe te voegen met een nog langere naam.


# Opdracht 9:
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.

# opgegeven_getal = 11
# while opgegeven_getal < 0 or opgegeven_getal > 10:
#     opgegeven_getal = int(input("Geef een getal op."))
#     if opgegeven_getal < 0 or opgegeven_getal > 10:
#         print("Dit is niet een van de getallen dat ik wil hebben.")


# Opdracht 10:
# repareer de volgende code:
MAX = 20
getal = int(input("Voer een getal in"))
if getal >> MAX:
    input(f"Het getal is groter dan {MAX}")
elif getal << MAX:
    input(f"Het getal is kleiner dan {MAX}")
else:
    input(f"Het getal is gelijk aan {MAX}")