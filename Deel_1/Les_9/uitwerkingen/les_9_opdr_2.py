# a = int(input("Vul een getal in. "))
# b = 7
# c = 11
# berekening_ab = b%a
# berekening_ac = c%a
# if berekening_ab != 0 and berekening_ac:
#     print(f"het getal {b} en {c} zijn niet zonder rest deelbaar")
# else:
#     print(f" {a} past zonder rest in {b} en {c} de heeft geen rest.")

a = int(input("Vul een getal in. "))
b = 7
c = 11
if b%a != 0 and c%a:
    print(f"het getal {b} en {c} zijn niet zonder rest deelbaar")
else:
    print(f" {a} past zonder rest in {b} en {c} de heeft geen rest.")