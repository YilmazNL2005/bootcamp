naam = input("Wat is je naam? ")
cijfer = int(input("Welk cijfer heb je gekregen? "))
if cijfer == 10:
    print("Uitmuntend")
if cijfer == 9:
    print("Zeer goed")
if cijfer == 8:
    print("Goed")
if cijfer == 7:
    print("Ruim voldoende")
if cijfer == 6:
    print("Voldoende")
if cijfer == 5:
    print("Bijna voldoende")
if cijfer == 4:
    print("Onvoldoende")
if cijfer == 3:
    print("Gering")
if cijfer == 2:
    print("Slecht")
if cijfer == 1:
    print("Zeer slecht")
if cijfer >= 6 <= 10:
    print("Gefeliciteerd, "+ str(naam) +" je resultaat is een " + str(cijfer))
else:
    print("Dit kan ik niet omzetten.")