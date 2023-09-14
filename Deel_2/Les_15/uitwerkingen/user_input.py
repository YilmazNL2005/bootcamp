def get_integer(prompt):
    vraag = int(input(prompt))
    return print(vraag)

get_integer(("Vul een getal in. "))

def get_float(prompt):
    vraag = float(input(prompt))
    return print(vraag)

get_float(("Vul een getal met getallen achter de komma in. "))

def get_string(prompt):
    vraag = input(prompt)
    return print(vraag)

get_string(("vul een woord in. "))

def get_letter(prompt):
    vraag = input(prompt)
    while len(vraag) > 1:
        vraag = input(prompt)
    return print(vraag.upper())

get_letter(("Vul max 1 letter in. "))