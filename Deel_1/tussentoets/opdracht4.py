oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig? '))
prijs_m2 = 40

if oppervlakte >= 150:
    prijs_m2 = 35
if oppervlakte >= 80 and oppervlakte < 150:
    prijs_m2 = 38
print(prijs_m2)
totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag is voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))