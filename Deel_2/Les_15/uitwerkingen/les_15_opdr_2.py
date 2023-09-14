def getallen(a, b):
    som_vermenigvuldigen = a * b
    return som_vermenigvuldigen

getal_a = int(input("Vul een getal in. "))
getal_b = int(input("Vul een getal in. "))

uitkomst = getallen(getal_a, getal_b)
print(f"De som van {getal_a} X {getal_b} = {uitkomst}")
