from time import sleep

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40
AANTAL_MELDINGEN_SLEEPS = 5

for x in range(AANTAL_MELDINGEN_SLEEPS):
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(AANTAL_MELDINGEN_SLEEPS)

# Het was niet helemaal duidelijk of de sleeps ook naar 5 gezet moesten worden of niet. 

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))
