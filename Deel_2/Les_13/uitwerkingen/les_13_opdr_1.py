kleuren = ("rood", "groen", "blauw", "roze", "oranje", "paars")
favoriete_kleur = input("Wat is je favoriete kleur? ")

if favoriete_kleur in kleuren:
    print(f"De kleur {favoriete_kleur} is onderdeel van de regenboog.")
else:
    print("Deze kleur is niet zo geweldig.")