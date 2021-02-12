firstInput = [4, 1, 3, 4, 3]

secondInput = [3, 2, 5, 1]  # should be len(firstInput[0])

time = 0

katSayisi = firstInput[0]

t1 = firstInput[1]  # asa
t2 = firstInput[2]  # murver asa
t3 = firstInput[3]  # kilic

katSuresi = firstInput[4]

# # Inputlari al
# ilkSatir = input().split()
# katSayisi = int(ilkSatir[0])
# t1 = int(ilkSatir[1]) # asa
# t2 = int(ilkSatir[2]) # murver
# t3 = int(ilkSatir[3]) # kilic
# katSuresi = int(ilkSatir[4])

# ikinciSatir = input().split()

# Input degerlerini kayd ediyoruz
katVeCanavar = {}
for i in range(katSayisi):
    katVeCanavar[i + 1] = {"Hortkuluk": 2,
                           "Canavar": secondInput[i]}

for i in range(1, katSayisi + 1):
    while True:
        # birinci kat icin
        olumYiyenSayisi = katVeCanavar[i]["Canavar"]
        hortkulukHP = katVeCanavar[i]["Hortkuluk"]

        if olumYiyenSayisi < t3:
            # asa kullan
            katVeCanavar[i]["Canavar"] = 0
            time += t1 * olumYiyenSayisi

        if olumYiyenSayisi > (2 * katSuresi):
            # murver asa kullan
            katVeCanavar[i]["Canavar"] = 0
            katVeCanavar[i]["Hortkuluk"] -= 1
            time += (t2 + katSuresi)

        if olumYiyenSayisi == 0 and hortkulukHP == 2:
            # kilic kullan
            katVeCanavar[i] = "DONE"
            time += (t3 + katSuresi)
            break

        if olumYiyenSayisi == 0 and hortkulukHP == 1:
            # asa kullan
            katVeCanavar[i] = "DONE"
            # kati degistir
            time += t1 + katSuresi
            break  # change
        if olumYiyenSayisi == 0 and hortkulukHP == 0:
            # kati degistir
            time += (katSuresi)
            katVeCanavar[i] = "DONE"
            break

    print(i)
    print(katVeCanavar)
    print(time)