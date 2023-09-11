oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig? '))
prijs_m2 = 40

if oppervlakte >= 150:
    prijs_m2 = 35
    totaal = prijs_m2 * oppervlakte
if oppervlakte >= 80 and oppervlakte < 150:
    prijs_m2 = 38
    totaal = prijs_m2 * oppervlakte

totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag is voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))