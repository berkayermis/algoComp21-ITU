cubukSayi = int(input())
cubukDegerleriSplit =  input().split()
cubukDegerleriToplam = 0

for i in cubukDegerleriSplit:
    cubukDegerleriToplam += int(i)

def enBuyukbolenTek(cubukDegerleriToplam):
    for i in range(1,100000000,2):
        if int(cubukDegerleriToplam) % i == 0:
            maxx = int(cubukDegerleriToplam) / i
    return int(maxx)

def enBuyukbolen(cubukDegerleriToplam):
    if cubukDegerleriToplam == 1:
        return 1

    elif cubukDegerleriToplam % 2 != 0:
        if cubukDegerleriToplam < 1099999999:
            for i in range(int(cubukDegerleriToplam / 2) - 1, 0, -2):
                if int(cubukDegerleriToplam) % i == 0:
                    return int(i)
        else:
            return enBuyukbolenTek(cubukDegerleriToplam)

    else:
        return int(cubukDegerleriToplam/2)


cubukSayisi = enBuyukbolen(cubukDegerleriToplam)
print(int(cubukDegerleriToplam / cubukSayisi))