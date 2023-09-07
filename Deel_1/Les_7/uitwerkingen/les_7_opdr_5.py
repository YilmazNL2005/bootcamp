begin_bedrag = 10000
aantal_jaar = 0
while aantal_jaar < 15:
    begin_bedrag = begin_bedrag / 100 * 102.8
    nieuw_bedrag = round(begin_bedrag, 2)
    aantal_jaar += 1
    print("Na "+ str(aantal_jaar)+ " krijg je "+str(nieuw_bedrag)+ " euro.")

# Na 5 jaar heb je 11.480,63 euro
# Na 15 jaar heb je 15.132,01 euro