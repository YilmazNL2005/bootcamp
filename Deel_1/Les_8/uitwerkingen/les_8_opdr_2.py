cijfer = int(input("Welk cijfer heb je gekregen? "))
omschrijving = ""
if cijfer == 10:
    omschrijving = "Uitmuntend"
if cijfer == 9:
    omschrijving = "Zeer goed"
if cijfer == 8:
    omschrijving = "Goed"
if cijfer == 7:
    omschrijving = "Ruim voldoende"
if cijfer == 6:
    omschrijving = "Voldoende"
if cijfer == 5:
    omschrijving = "Bijna voldoende"
if cijfer == 4:
    omschrijving = "Onvoldoende"
if cijfer == 3:
    omschrijving = "Gering"
if cijfer == 2:
    omschrijving = "Slecht"
if cijfer == 1:
    omschrijving = "Zeer slecht"
if cijfer >= 6 <= 10:
    omschrijving = "Gefeliciteerd, "+ str(omschrijving) +" je resultaat is een " + str(cijfer)
else:
    print("Dit kan ik niet omzetten.")