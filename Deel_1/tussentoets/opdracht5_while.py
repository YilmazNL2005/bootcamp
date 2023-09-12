from time import sleep

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40
AANTAL_MELDINGEN_SLEEPS = 5
gegeven_meldingen = 0
while gegeven_meldingen < AANTAL_MELDINGEN_SLEEPS:
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(1)
    gegeven_meldingen = gegeven_meldingen + 1

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))