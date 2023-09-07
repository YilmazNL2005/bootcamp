a = int(input("Vul een getal in. "))
b = int(input("Vul een getal in. "))

if a > b:
    print("Variabele a is het grootst want " + str(a) + " is groter dan " + str(b))
if b > a:
    print("Variabele b is het grootst want " + str(b) + " is groter dan " + str(a))
if a < b:
    print("Variabele a is het kleinste want " + str(a) + " is kleiner dan " + str(b))
if b < a:
    print("Variabele a is het kleinste want " + str(b) + " is kleiner dan " + str(a))
if a == b:
    print("a is gelijk aan b. ")
else:
    print("b is gelijk aan a.")