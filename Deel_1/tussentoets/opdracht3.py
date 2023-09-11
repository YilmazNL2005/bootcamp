naam = input("Wat is je naam? ")
leeftijd = int(input("Wat is je leeftijd in jaren? "))

if leeftijd < 18:
    print(f"Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in :-(")
else:
    print(f"Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).")