leeftijd = int(input("Wat is je leeftijd?"))
snor = input("Heb je een snor? ja/nee ")
diploma = input("Heb je een diploma? ja/nee ")
if leeftijd >= 18 and snor == "ja" or diploma == "ja" and leeftijd < 18:
    print("Je bent aangenomen!!!")
