def get_integer(prompt):
    while True:
        try:
            vraag = int(input(prompt))
            return print(vraag)
        except ValueError:
            print("Dit is geen getal. ")

get_integer(("Vul een getal in. "))

def get_float(prompt):
    while True:
        try:
            vraag = float(input(prompt))
            return print(vraag)
        except ValueError:
            print("Dit is geen getal. ")

get_float(("Vul een getal met getallen achter de komma in. "))