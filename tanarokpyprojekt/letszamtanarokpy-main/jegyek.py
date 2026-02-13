import random
import math
def Jegyek():
    letszam = int(input("Adja meg az osztály létszámát: "))
    jegyek = []
    for i in range(letszam):
        jegy = random.randint(1,10)
        jegyek.append(jegy)
    atlag = sum(jegyek) / letszam
    bukott = 0
    voltekituno = False
    volteegyes = False
    for jegy in jegyek:
        if jegy < 4:
            bukott += 1
        if jegy == 10:
            voltekituno = True
        if jegy == 1:
            volteegyes = True
    print(f"Jegyek: {jegyek}")
    print(f"Átlag: {round(atlag)}")
    print(f"Bukott diákok száma: {bukott}")
    print(f"Volt-e 1-es osztályzat: {'Igen' if volteegyes else 'Nem'}")
    print(f"Van-e kitűnő jegy: {'Van' if voltekituno else 'Nincs'}")

Jegyek()
