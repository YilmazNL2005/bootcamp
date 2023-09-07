a = int(input("Vul een getal in. "))
b = int(input("Vul een getal in. "))
c = int(input("Vul een getal in. "))

# a = 1
# b = 2
# c = 3

if a > b and a > c:
    print("Variabele a is het grootst want " + str(a) + " is groter dan " + str(b) + " en " + str(c))
if b > a and b > c:
    print("Variabele b is het grootst want " + str(b) + " is groter dan " + str(a) + " en " + str(c))
if c > a and c > b:
    print("Variabele c is het grootst want " + str(c) + " is groter dan " + str(a) + " en " + str(b))
if a == b == c:
    print("Variabele a, b en c zijn gelijk aan elkaar.")